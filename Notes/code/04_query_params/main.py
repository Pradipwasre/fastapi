from fastapi import FastAPI

app = FastAPI()


# ──────────────────────────────────────────────
# Example 1 - Filter students by city
#
# city is NOT inside {} in the route.
# So FastAPI treats it as a query parameter automatically.
#
# Test: GET http://127.0.0.1:8000/students?city=Mumbai
# Test: GET http://127.0.0.1:8000/students?city=Pune
# ──────────────────────────────────────────────

@app.get("/students")
def get_students(city: str):
    return {"city": city, "count": 25}


# ──────────────────────────────────────────────
# Example 2 - Optional query params with default values
#
# Adding a default value makes the param optional.
# If not provided in the URL, the default is used.
#
# Test: GET http://127.0.0.1:8000/products
# Test: GET http://127.0.0.1:8000/products?brand=Apple
# Test: GET http://127.0.0.1:8000/products?brand=Apple&limit=5
# ──────────────────────────────────────────────

@app.get("/products")
def get_products(brand: str = "all", limit: int = 10):
    return {"brand": brand, "limit": limit}


# ──────────────────────────────────────────────
# Example 3 - Dataset filter (ML context)
#
# When Streamlit calls FastAPI to fetch filtered training data,
# this is the exact pattern used.
#
# Test: GET http://127.0.0.1:8000/data
# Test: GET http://127.0.0.1:8000/data?label=diabetic
# Test: GET http://127.0.0.1:8000/data?label=diabetic&rows=50
# ──────────────────────────────────────────────

@app.get("/data")
def get_data(label: str = "all", rows: int = 100):
    return {
        "label": label,
        "rows_fetched": rows,
        "source": "diabetes_dataset.csv"
    }


# ──────────────────────────────────────────────
# Bonus - Combining path param and query param in one route
#
# Path param identifies which dataset.
# Query param filters how many rows to return.
#
# Test: GET http://127.0.0.1:8000/data/diabetes?rows=50
# Test: GET http://127.0.0.1:8000/data/titanic?rows=200
# ──────────────────────────────────────────────

@app.get("/data/{dataset}")
def get_dataset(dataset: str, rows: int = 100):
    return {
        "dataset": dataset,
        "rows": rows
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
#   Create GET /orders with query param status (default "all")
#   Return {"status": status, "count": 42}
#
# Task 2:
#   Create GET /search with query params keyword (str) and page (int, default 1)
#   Return the keyword and page number
#
# Task 3:
#   Create GET /predictions/{model_name} with query param threshold (float, default 0.5)
#   Return model_name and threshold
#   This simulates fetching predictions from a specific model with a custom confidence threshold
# ──────────────────────────────────────────────
