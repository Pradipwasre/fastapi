from fastapi import FastAPI

app = FastAPI()


# ──────────────────────────────────────────────
# Example 1 - Return a simple message
# Test: GET http://127.0.0.1:8000/
# ──────────────────────────────────────────────

@app.get("/")
def home():
    return {"msg": "Hello from FastAPI"}


# ──────────────────────────────────────────────
# Example 2 - Return a list of students
# Test: GET http://127.0.0.1:8000/students
# ──────────────────────────────────────────────

@app.get("/students")
def get_students():
    data = [
        {"id": 1, "name": "Rahul"},
        {"id": 2, "name": "Priya"},
        {"id": 3, "name": "Amit"}
    ]
    return data


# ──────────────────────────────────────────────
# Example 3 - Return ML model information
# This is how Streamlit will check which model is running
# Test: GET http://127.0.0.1:8000/model-info
# ──────────────────────────────────────────────

@app.get("/model-info")
def model_info():
    return {
        "model": "Random Forest",
        "accuracy": 0.92,
        "status": "ready"
    }


# ──────────────────────────────────────────────
# Run the server:
#   uvicorn main:app --reload
#
# Open Swagger:
#   http://127.0.0.1:8000/docs
# ──────────────────────────────────────────────

# ──────────────────────────────────────────────
# Practice Tasks
#
# Task 1:
#   Add a new GET route /teachers
#   Return a list of 3 teacher names as a list of dicts
#
# Task 2:
#   Add a GET route /dataset-info
#   Return name, rows, and columns of any dataset you know
#   Example: Titanic dataset has 891 rows and 12 columns
#
# Task 3:
#   Add a GET route /health
#   Return {"status": "ok", "server": "running"}
#   This type of endpoint is used in production to check if the API is alive
# ──────────────────────────────────────────────
