# AI CRM

A full-stack CRM application built using React, FastAPI, and SQLite.

## Features

- Add Customers
- View Customers
- Update Customers
- Delete Customers
- Persistent Database Storage

## Tech Stack


### Frontend
- React
- Vite

### Backend
- FastAPI
- SQLAlchemy

### Database
- SQLite

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

## Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install fastapi uvicorn sqlalchemy

python -m uvicorn main:app --reload
```

---

## API Endpoints

- GET /customers
- POST /customers
- PUT /customers/{id}
- DELETE /customers/{id}