# Items Manager Architecture

A comprehensive, dependency-free full-stack web application built from scratch to demonstrate fundamental software engineering principles.

## 🚀 Project Overview

The **Items Manager** is a complete, production-ready web application built entirely without external frameworks. It evolved through 15 structured phases, starting from simple in-memory models and scaling up to a cloud-ready, dockerized architecture.

The core functionality allows authenticated users to create, manage, and transition items through a strict business workflow (`draft` -> `active` -> `completed` / `blocked`).

## 🛠️ Technology Stack

- **Backend:** Vanilla Python 3.11 (`http.server`)
- **Database:** SQLite3 (Standard Library)
- **Frontend:** Vanilla JavaScript (ES6), HTML5, CSS3
- **Authentication:** Custom stateless JWT (JSON Web Tokens) using HMAC-SHA256
- **Deployment:** Docker & Docker Compose
- **CI/CD:** GitHub Actions

*Zero external dependencies were used in the application runtime.*

---

## 📈 The Journey (Phases 1-15)

This repository is organized into phases, demonstrating the logical progression of software complexity:

1. **Phases 1-4 (The Foundation):** In-memory data models, basic CRUD operations, and core logic.
2. **Phases 5-7 (Persistence & Architecture):** Introduction of SQLite, the Repository Pattern, and Dependency Injection.
3. **Phases 8-10 (Business Logic & Security):** Implementation of strict state machine workflows, Data Validation, and User Authentication.
4. **Phases 11-13 (Web & API):** Transition to a RESTful API layer and a fully responsive Vanilla JS Frontend UI.
5. **Phases 14-15 (Cloud & DevOps):** External configuration via `.env`, Docker packaging, Nginx Load Balancing, and CI/CD pipelines.

---

## 💻 How to Run the Application

You can run the application either directly on your local machine or using Docker.

### Option 1: Run Locally (Python)

1. **Navigate to the latest phase** (Phase 15):
   ```bash
   cd phase_15
   ```
2. **Setup your environment variables**:
   Copy the example environment file:
   ```bash
   cp .env.example .env.development
   ```
3. **Start the server**:
   ```bash
   python main.py
   ```
4. **Open your browser**:
   Navigate to `http://127.0.0.1:8000`

### Option 2: Run via Docker (Production Simulation)

To run the application behind an Nginx Load Balancer with auto-scaling instances:

1. **Navigate to Phase 15**:
   ```bash
   cd phase_15
   ```
2. **Spin up the cluster**:
   ```bash
   docker-compose up -d --build
   ```
3. **Access the application**:
   Navigate to `http://localhost`

---

## 🧪 Testing

The project includes a comprehensive suite of automated unit and integration tests.

```bash
cd phase_15
python -m unittest discover -s tests -v
```

## 🔒 Features Highlight

- **State Machine Workflow:** Items must follow a strict path (`draft` -> `active`). History is tracked in an immutable ledger.
- **Stateless Authentication:** Custom-built JWT authentication mechanism injected automatically via JS interceptors.
- **Dynamic Frontend:** Single-page-like experience built with pure JS components (Toasts, Modals, Spinners).
- **Environment Agnostic:** Seamlessly transitions between `development` and `production` modes dynamically based on `.env` injection.
