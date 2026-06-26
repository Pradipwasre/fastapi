from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ──────────────────────────────────────────────
# Example 1 - Receive a name, return a greeting
#
# Step 1: Define what data you expect using BaseModel
# Step 2: FastAPI validates the incoming JSON automatically
#
# Test: POST http://127.0.0.1:8000/greet
# Body: {"name": "Rahul"}
# ──────────────────────────────────────────────

class User(BaseModel):
    name: str


@app.post("/greet")
def greet(user: User):
    return {"msg": f"Hello {user.name}!"}


# ──────────────────────────────────────────────
# Example 2 - Add two numbers
#
# Same pattern as ML prediction.
# Input goes in, result comes out.
# Replace the addition with model.predict() later.
#
# Test: POST http://127.0.0.1:8000/add
# Body: {"a": 10, "b": 25}
# ──────────────────────────────────────────────

class Nums(BaseModel):
    a: float
    b: float


@app.post("/add")
def add(data: Nums):
    result = data.a + data.b
    return {"result": result}


# ──────────────────────────────────────────────
# Example 3 - Disease prediction (ML deployment pattern)
#
# This is the real pattern you will use when deploying your model.
# Right now it uses a simple rule.
# In the actual project, replace the rule with:
#   result = model.predict([[p.age, p.bp, p.cholesterol]])
#
# Test: POST http://127.0.0.1:8000/predict
# Body: {"age": 55, "bp": 140, "cholesterol": 230}
# ──────────────────────────────────────────────

class Patient(BaseModel):
    age: int
    bp: int
    cholesterol: int


@app.post("/predict")
def predict(p: Patient):
    # Replace this line with your actual model prediction later
    result = "High Risk" if p.age > 50 else "Low Risk"
    return {"prediction": result}


# ──────────────────────────────────────────────
# Run the server:
#   uvicorn main:app --reload
#
# Open Swagger:
#   http://127.0.0.1:8000/docs
#
# In Swagger, click any POST endpoint, click "Try it out",
# paste the JSON body, and click Execute.
# ──────────────────────────────────────────────

# ──────────────────────────────────────────────
# Practice Tasks
#
# Task 1:
#   Create a BaseModel called Student with fields: name (str), marks (int)
#   Create a POST route /result
#   If marks >= 40 return {"result": "Pass"} else {"result": "Fail"}
#
# Task 2:
#   Create a BaseModel called Rectangle with fields: length (float), width (float)
#   Create a POST route /area
#   Return the area and perimeter of the rectangle
#
# Task 3:
#   Create a BaseModel called House with fields: size (int), location (str), age (int)
#   Create a POST route /price-estimate
#   Return a dummy estimated price based on any logic you like
#   This simulates a house price prediction model
# ──────────────────────────────────────────────
