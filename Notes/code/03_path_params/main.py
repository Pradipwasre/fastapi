from fastapi import FastAPI

app = FastAPI()


# ──────────────────────────────────────────────
# Example 1 - Get student by ID
#
# {sid} in the route means it is a path parameter.
# FastAPI extracts the value from the URL and passes it to the function.
# It also converts it to int automatically.
#
# Test: GET http://127.0.0.1:8000/student/101
# Test: GET http://127.0.0.1:8000/student/205
# Try:  GET http://127.0.0.1:8000/student/abc  (will give validation error)
# ──────────────────────────────────────────────

@app.get("/student/{sid}")
def get_student(sid: int):
    return {"student_id": sid, "name": "Rahul"}


# ──────────────────────────────────────────────
# Example 2 - Get product by name
#
# Path parameter can also be a string.
# The value from the URL is passed directly to the function.
#
# Test: GET http://127.0.0.1:8000/product/laptop
# Test: GET http://127.0.0.1:8000/product/phone
# ──────────────────────────────────────────────

@app.get("/product/{name}")
def get_product(name: str):
    return {"product": name, "price": 999}


# ──────────────────────────────────────────────
# Example 3 - Get ML model by version
#
# In production, you may have multiple model versions deployed.
# The client can request a specific version using the path param.
#
# Test: GET http://127.0.0.1:8000/model/1
# Test: GET http://127.0.0.1:8000/model/2
# Test: GET http://127.0.0.1:8000/model/5
# ──────────────────────────────────────────────

@app.get("/model/{version}")
def get_model(version: int):
    return {
        "version": version,
        "type": "Random Forest",
        "accuracy": round(0.90 + (version * 0.01), 2)
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
#   Create GET /order/{order_id}
#   Return order_id and a status of "Processing"
#
# Task 2:
#   Create GET /city/{city_name}
#   Return city_name and a dummy population number
#
# Task 3:
#   Create GET /experiment/{exp_id}
#   Return exp_id, model used, and a dummy accuracy value
#   This simulates fetching an ML experiment result by ID
# ──────────────────────────────────────────────
