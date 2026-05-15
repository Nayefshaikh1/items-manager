# Phase 14 — Production Readiness & Deployment

## 1. Environment Configurations
The application separates configuration from logic using `.env` files. 

- **`.env.development`**: Used for local work. Uses local sqlite files, enables debug logs, and has relaxed security settings.
- **`.env.production`**: Used for real deployments. Binds to `0.0.0.0`, reduces logging noise to `INFO`, and requires a strong `SECRET_KEY`.

**To switch environments:** Set `APP_ENV=production` in your system's environment variables.

## 2. Packaging (Docker)
A `Dockerfile` is provided for reproducible deployments.
```bash
# Build the image
docker build -t items-manager:1.0 .

# Run in production mode with a real secret and persistent database volume
docker run -d \
  -p 8000:8000 \
  -e APP_ENV=production \
  -e SECRET_KEY="your_secure_secret_here" \
  -v /path/to/local/data:/app/database.db \
  items-manager:1.0
```

## 3. Production Logging
Generic `print()` statements have been replaced with Python's standard `logging` module. 
- In development, it logs verbose debug information.
- In production, it only logs `INFO` and `ERROR` events to keep logs clean, useful, and avoid leaking PII or internal payload structures.

## 4. Health Checks
A `/health` endpoint is available to verify the application's liveness and its ability to connect to the database.
```bash
# Test the health check
curl http://127.0.0.1:8000/health

# Expected response:
# {"success": true, "data": {"status": "ok", "database": "connected"}}
```

## 5. Deployment Verification & Rollback
When deploying a new version, perform these checks:
1. **Liveness**: Ensure the container starts and `GET /health` returns `200 OK`.
2. **Readiness**: Verify the UI loads correctly and static files serve without 404s.
3. **Core Path**: Create a single item to ensure database write access and workflow history are functioning.

**Rollback Plan**:
If `GET /health` fails, or if errors spike in the logs immediately after deployment:
1. Immediately stop the new container.
2. Revert to the previous Docker image tag (`docker run ... items-manager:0.9`).
3. If database schemas were altered, restore the `.db` file from the pre-deployment backup.
