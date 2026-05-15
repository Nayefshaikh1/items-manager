# Phase 15 — Cloud and Infrastructure Architecture

This document defines the high-level cloud deployment target, network layout, compute/storage infrastructure, and operational lifecycle for the Items Manager application.

---

## Task 1: Deployment Target & Environment Model

The system is no longer viewed as a local project but as a distributed application running on cloud infrastructure. 

### Environments
The application will operate across four isolated environments:
1. **Development (Local):** Runs on developer machines using `.env.development`. Uses local SQLite and default `8000` ports.
2. **Test/QA:** An ephemeral cloud environment spun up during CI/CD to run automated tests. Uses a mock database and is destroyed after tests complete.
3. **Staging:** A persistent cloud environment mirroring Production exactly (same OS, same managed DB tier, same network rules). Used for final human QA and UAT. Connects to a `staging` database.
4. **Production:** The live, customer-facing environment. Connects to the `production` managed database. Uses strict security groups and `.env.production`.

**Key Boundary:** No business logic relies on environment-specific knowledge. Environment context is injected entirely via configuration.

---

## Task 2: Network Layout & Access Boundaries

The application is split into Public and Private zones using virtual networking (e.g., AWS VPC).

### Boundaries
- **Public Zone (DMZ):**
  - **Load Balancer (ALB/Nginx):** The ONLY component exposed to the public internet (Ports 80/443).
  - Routes traffic to the backend instances based on path routing.
- **Private Zone:**
  - **Compute Instances (Backend/API/UI Server):** Cannot be reached directly from the internet. They only accept traffic from the Load Balancer.
  - **Database Subnet:** Completely isolated. Only accepts traffic from the Compute Instances. No direct internet access.
  - **Secrets Manager:** An internal VPC endpoint to securely fetch secrets at runtime.

---

## Task 3: Compute Layer

The application will run inside Docker containers hosted on a managed compute service (e.g., AWS ECS, Google Cloud Run, or a basic Auto Scaling Group of VMs).

### Runtime Behavior
- **Stateless Execution:** The compute instances hold no persistent data. If a container dies, a new one spins up without data loss.
- **Single Artifact:** The exact same Docker image built in CI is promoted through Test -> Staging -> Production. Only the injected `.env` variables change.
- **Process Management:** A process manager (like Docker daemon) ensures the application stays online and restarts upon failure.

---

## Task 4: Managed Database & Storage

Because compute instances are ephemeral, we must move away from local `.db` files attached to a single disk.

### Cloud Storage Strategy
- **Primary Database:** A Managed Relational Database (e.g., AWS RDS for PostgreSQL/MySQL). 
  - *Why?* Managed databases handle automated daily backups, point-in-time recovery, and multi-zone durability. The application connects via a standard connection string provided in the config.
- **Object Storage (Optional for future):** If items require image attachments later, they will be stored in an Object Store (like AWS S3), saving only the URL in the database. 
- **Durability:** Data survives server restarts because the compute layer and the storage layer are physically decoupled.

---

## Task 5: Configuration, Secrets, & Identity

Security and configuration must be decoupled from the application codebase.

### Handling Non-Code Values
- **Public Config:** Non-sensitive values (like `LOG_LEVEL=INFO`, `APP_PORT=8000`) are passed as standard environment variables via the compute orchestrator.
- **Secrets:** Sensitive values (like `SECRET_KEY`, Database Passwords) are NEVER stored in code or plain text. They are stored in a managed secrets vault (e.g., AWS Secrets Manager or HashiCorp Vault) and fetched dynamically at startup, or injected securely into the container environment.
- **Identity (IAM):** The compute instance running the application is assigned a temporary "Role". This role is granted explicit permission to access the Secrets vault and the Database. It has no permissions to access unrelated cloud services.

---

## Task 6: Deployment & Release Flow

Releases are automated, predictable, and reversible.

### CI/CD Pipeline
1. **Commit:** Developer pushes code to `main`.
2. **Build & Test:** CI server builds the Docker image and runs unit tests. If tests pass, the image is pushed to a Container Registry.
3. **Deploy to Staging:** CD pipeline pulls the image, injects staging secrets, and spins it up. QA performs checks.
4. **Deploy to Production (Promotion):** The EXACT same image is promoted to production. 
5. **Rollback:** If health checks fail post-deployment, the load balancer automatically routes traffic back to the previous stable container image.

---

## Task 7: Scaling & Resilience

The system must handle increased load and survive underlying hardware failures gracefully.

- **Horizontal Scaling:** When CPU utilization hits 70%, the auto-scaler automatically spins up additional identical containers. The Load Balancer distributes traffic evenly among them.
- **Redundancy:** Containers are distributed across multiple physically separated data centers (Availability Zones). If one data center goes offline, the others take the load.
- **Graceful Degradation:** If the database goes offline, the application's `/health` endpoint reports failure. The Load Balancer will serve a friendly "Maintenance" page instead of returning raw stack traces to users.

---

## Task 8: End-to-End Operational Review

### The Request Lifecycle
1. User requests `http://items-manager.com/`.
2. Traffic hits the **Public Load Balancer**, protecting backend servers from direct attack.
3. The Load Balancer routes traffic to a **Compute Container** in the Private Subnet.
4. The Container (running our Phase 14 Python code) processes the request, utilizing the `SECRET_KEY` injected securely via the **Secrets Manager**.
5. If data is needed, the Container queries the **Managed Database**, which sits in an even deeper, isolated subnet.
6. The container responds. If traffic spikes, an **Auto-Scaler** spins up a clone of the container seamlessly.

The application is now conceptually ready for enterprise-grade Cloud-Native deployment.
