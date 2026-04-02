# Finance Backend API (Zorvyn Assignment)

## Overview

This project is a backend system for managing financial records with role-based access control. It allows users to create, manage, and analyze financial data based on their roles.

---

## Features

* User Management (Admin, Analyst, Viewer)
* Financial Records (CRUD operations)
* Role-Based Access Control (RBAC)
* Dashboard Summary APIs
* Input Validation and Error Handling
* Filtering and Query Support

---
##  Demo

- Admin can create/delete records
- Analyst can view summary
- Viewer is restricted from modifying data

  
## 🛠 Tech Stack

* FastAPI
* SQLite
* SQLAlchemy
* Pydantic

---

##  Roles & Permissions

| Role    | Permissions            |
| ------- | ---------------------- |
| Admin   | Full access            |
| Analyst | View records + summary |
| Viewer  | View only              |

---

## 📊 API Endpoints

### Users

* POST /users
* GET /users

### Records

* POST /records
* GET /records
* DELETE /records/{id}

### Dashboard

* GET /summary

---

## How to Run

```bash
uvicorn main:app --reload
```

---

##  Notes

* Role-based access is implemented using FastAPI dependencies
* SQLite is used for simplicity
* Validation handled using Pydantic

---

##  Author

Umer Rafiq
