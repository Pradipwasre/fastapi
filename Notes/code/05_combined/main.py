from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ──────────────────────────────────────────────
# This file puts all Day 1 concepts together.
# Run this at the end of class to review everything.
#
# Run: uvicorn main:app --reload
# Docs: http://127.0.0.1:8000/docs
# ──────────────────────────────────────────────


# ──────────────────────────
# GET - Simple message
# Test: GET /
# ──────────────────────────

@app.get("/")
def home():
    return {"msg": "FastAPI server is running"}


# ──────────────────────────
# GET - Return model info
# Test: GET /model-info
# ──────────────────────────

@app.get("/model-info")
def model_info():
    return {
        "model": "Random Forest",
        "accuracy": 0.92,
        "status": "ready"
    }


# ──────────────────────────
# GET with Path Parameter - Get student by ID
# Test: GET /student/101
# ──────────────────────────

@app.get("/student/{sid}")
def get_student(sid: int):
    return {"student_id": sid, "name": "Rahul"}


# ──────────────────────────
# GET with Query Parameter - Filter students
# Test: GET /students
# Test: GET /students?city=Pune
# Test: GET /students?city=Mumbai&limit=5
# ──────────────────────────

@app.get("/students")
def get_students(city: str = "all", limit: int = 10):
    return {"city": city, "limit": limit}


# ──────────────────────────
# GET with Path + Query - Dataset with filter
# Test: GET /data/diabetes
# Test: GET /data/diabetes?rows=50
# ──────────────────────────

@app.get("/data/{dataset}")
def get_data(dataset: str, rows: int = 100):
    return {"dataset": dataset, "rows_fetched": rows}


# ──────────────────────────
# POST - Simple greeting
# Test: POST /greet
# Body: {"name": "Rahul"}
# ──────────────────────────

class User(BaseModel):
    name: str


@app.post("/greet")
def greet(user: User):
    return {"msg": f"Hello {user.name}!"}


# ──────────────────────────
# POST - ML Prediction Pattern
# This is the skeleton of your final project.
# Test: POST /predict
# Body: {"age": 55, "bp": 140, "cholesterol": 230}
# ──────────────────────────

class Patient(BaseModel):
    age: int
    bp: int
    cholesterol: int


@app.post("/predict")
def predict(p: Patient):
    # In the real project this line becomes:
    # result = model.predict([[p.age, p.bp, p.cholesterol]])
    result = "High Risk" if p.age > 50 else "Low Risk"
    return {"prediction": result}


# ──────────────────────────────────────────────
# Final Practice Task - Build your own mini API
#
# Create a new file called my_api.py in this folder.
# Build a FastAPI app that has:
#
#   1. GET /          returns your name and today's topic
#   2. GET /student/{roll}   returns the roll number and a dummy student name
#   3. GET /courses   with optional query param language (default "Python")
#                     returns the language and a list of 3 course names
#   4. POST /score    accepts name (str) and marks (int)
#                     returns Pass if marks >= 40 else Fail
#
# Run it with: uvicorn my_api:app --reload
# Test everything in Swagger at http://127.0.0.1:8000/docs
# ──────────────────────────────────────────────
