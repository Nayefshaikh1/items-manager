# 🚀 Items Manager (Python)

## 📌 Overview

This project is a step-by-step implementation of an **Items Manager** built using Python.

It demonstrates how backend systems evolve from:

* simple CRUD operations
* to clean architecture
* to persistence
* to object-oriented design
* to **real-world scalable architecture**

---

## ⚙️ Features

### ✅ Phase 1 – Basic CRUD

* Create item
* List all items
* Find item by ID
* Update item
* Delete item

---

### 🔥 Phase 2 – Clean Design

* Separation of concerns
* Helper functions
* Validation
* Error handling

---

### 💾 Phase 3 – Persistence

* JSON file storage
* Load data on startup
* Storage abstraction

---

### 🧠 Phase 4 – Object-Oriented Architecture

* Item as a domain entity (data + behavior)
* Service layer for business logic
* Store layer for collection management
* Dependency injection (composition)
* Clean separation of responsibilities

---

### 🚀 Phase 5 – Scalable Architecture (Industry Level)

* Repository pattern (data access abstraction)
* Service layer decoupled from storage
* Dependency inversion (interface-based design)
* Replaceable storage (file → database ready)
* Unit testing (service layer with fake repository)
* Integration testing (repository with real storage)

---

## 🧠 Concepts Covered

* Data Modeling
* CRUD Operations
* DRY Principle
* Separation of Concerns
* Validation & Error Handling
* Abstraction
* Persistence
* Object-Oriented Design
* Dependency Injection
* Clean Architecture
* Repository Pattern
* Dependency Inversion Principle (DIP)
* Unit Testing & Integration Testing

---

## 📁 Project Structure

```text
items-manager/
│
├── phase_1/
│   ├── items_manager.py
│   └── test_phase1.py
│
├── phase_2/
│   ├── item.py
│   ├── manager.py
│   └── test_phase2.py
│
├── phase_3/
│   ├── item.py
│   ├── manager.py
│   ├── storage_base.py
│   ├── file_storage.py
│   └── test_phase3.py
│
├── phase_4/
│   ├── item.py
│   ├── item_service.py
│   ├── item_store.py
│   ├── storage.py
│   └── tests/
│       └── test_phase4.py
│
├── phase_5/
│   ├── item.py
│   ├── item_service.py
│   ├── item_repository.py
│   ├── file_repository.py
│   ├── storage.py
│   └── tests/
│       ├── test_service.py
│       └── test_repository.py
│
└── README.md
```

---

## ▶️ How to Run

## ▶️ How to Run

### Phase 1

```
cd phase_1
python test_phase1.py
```

### Phase 2

```
cd phase_2
python test_phase2.py
```

### Phase 3

```
cd phase_3
python test_phase3.py
```

### Phase 4

```
cd phase_4
python main.py
```

### Phase 5

```bash
cd phase_5
python main.py
```

Run tests:

```bash
python -m unittest discover -s tests -v
```

---

## 🧪 Testing Strategy

* **Unit Tests** → Service layer (using fake repository)
* **Integration Tests** → Repository layer (real file storage)
* **Coverage Ready** → Can measure using `coverage`

---

## 🎯 Design Summary

* **Item** → owns data and behavior
* **Service** → controls business logic
* **Repository** → abstracts data access
* **Storage** → handles persistence
* **Main** → wires dependencies (composition root)

---

## 🚀 Learning Outcome

Through this project, I learned:

* How to evolve a system from simple scripts to scalable architecture
* How to separate business logic from data access
* How to design flexible systems using dependency injection
* How to apply repository pattern in real applications
* How to test systems using unit and integration testing

---

## 🔗 GitHub Repository

👉 https://github.com/Nayefshaikh1/items-manager

---

## 📢 About Me

I am learning backend development and sharing my progress through real-world projects.

---

#Python #BackendDevelopment #LearningInPublic #SoftwareEngineering #CleanCode #OOP #SystemDesign #Testing #Architecture



I am learning backend development and sharing my progress through real-world projects.

---

#Python #BackendDevelopment #LearningInPublic #SoftwareEngineering #CleanCode #OOP #SystemDesigns
