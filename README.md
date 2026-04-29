# 🚀 Items Manager (Python)

## 📌 Overview

This project is a step-by-step implementation of an **Items Manager** built using Python.

It demonstrates how backend systems evolve from:

* simple CRUD operations
* to clean architecture
* to persistence
* to object-oriented design

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

---

## 📁 Project Structure

```
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
│   ├── item.py              # Entity
│   ├── item_service.py      # Business logic
│   ├── item_store.py        # Collection layer
│   ├── storage.py           # Persistence
│   └── tests/
│       └── test_phase4.py
│
└── README.md
```

---

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

Run tests:

```
python -m unittest discover
```

---

## 📸 Output Example

Add your output screenshot in:

```
assets/output.png
```

---

## 🧠 Learning Outcome

Through this project, I learned:

* How backend systems evolve from simple scripts to structured architecture
* How to separate concerns across layers (Entity, Service, Storage)
* How to design maintainable and scalable systems
* How persistence works using JSON
* How dependency injection improves flexibility and testability

---

## 🎯 Design Summary

* **Item** → owns data and behavior
* **Service** → controls operations
* **Store** → manages collection
* **Storage** → handles persistence

---

## 🔗 GitHub Repository

👉 https://github.com/Nayefshaikh1/items-manager

---

## 📢 About Me

I am learning backend development and sharing my progress through real-world projects.

---

#Python #BackendDevelopment #LearningInPublic #SoftwareEngineering #CleanCode #OOP #SystemDesign


I am learning backend development and sharing my progress through real projects.

---

#Python #BackendDevelopment #LearningInPublic #SoftwareEngineering #CleanCode
