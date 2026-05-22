from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from langgraph_workflow import workflow

from database import SessionLocal, engine, Base
from models import Customer

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "API running successfully"}

@app.get("/customers")
def get_customers():
    db: Session = SessionLocal()

    customers = db.query(Customer).all()

    result = []

    for customer in customers:
        result.append({
            "id": customer.id,
            "name": customer.name,
            "email": customer.email
        })

    db.close()

    return result

@app.post("/customers")
def add_customer(customer: dict):
    db: Session = SessionLocal()

    new_customer = Customer(
        name=customer["name"],
        email=customer["email"]
    )

    db.add(new_customer)

    db.commit()

    db.refresh(new_customer)

    db.close()

    return {
        "message": "Customer added successfully"
    }
@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int):
    db: Session = SessionLocal()

    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if customer:
        db.delete(customer)
        db.commit()

    db.close()

    return {
        "message": "Customer deleted successfully"
    }
@app.put("/customers/{customer_id}")
def update_customer(customer_id: int, updated_data: dict):
    db: Session = SessionLocal()

    customer = db.query(Customer).filter(
        Customer.id == customer_id
    ).first()

    if customer:
        customer.name = updated_data["name"]
        customer.email = updated_data["email"]

        db.commit()

    db.close()

    return {
        "message": "Customer updated successfully"
    }
@app.post("/analyze")
def analyze_customer(data: dict):

    result = workflow.invoke({
        "customer_name": data["name"],
        "customer_email": data["email"],
        "analysis": ""
    })

    return {
        "analysis": result["analysis"]
    }