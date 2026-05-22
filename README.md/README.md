# AI CRM

A full-stack AI-powered CRM application built using React, FastAPI, SQLite, SQLAlchemy, and LangGraph.

## Features

- Add Customers
- View Customers
- Update Customers
- Delete Customers
- Persistent Database Storage
- AI Lead Analysis
- LangGraph Workflow Integration

---

## Tech Stack

### Frontend
- React
- Vite

### Backend
- FastAPI
- SQLAlchemy

### Database
- SQLite

### AI Workflow
- LangGraph
- LangChain

---

## LangGraph Workflow

The project includes a LangGraph workflow with 5 tools/nodes:

1. Create Customer Tool
2. Read Customer Tool
3. Update Customer Tool
4. Delete Customer Tool
5. Analyze Customer Tool

The workflow performs customer lead analysis and classification.

---

## Frontend Setup

```bash
cd frontend
npm install
npm run dev