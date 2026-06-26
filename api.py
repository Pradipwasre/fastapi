from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# ==============================================================
# HOW TO RUN THIS FILE
#
#   uvicorn api:app --reload
#
# HOW TO TEST
#
#   Open browser and go to:
#   http://127.0.0.1:8000/docs
#
# That page is called Swagger UI.
# Every endpoint you write below will appear there automatically.
# You can test everything from that page directly.
# ==============================================================




# ==============================================================
# SECTION 1 - GET REQUEST
#
# GET is used to READ data from the server.
# You are not creating or changing anything. Just fetching.
#
# Real world: Like asking "show me the menu."
# You are only reading. Nothing changes on the server.
# ==============================================================


# GET Example 1 - Return a simple message
# Test URL: http://127.0.0.1:8000/

@app.get("/")
def home():
    return {"msg": "Hello from FastAPI"}


# GET Example 2 - Return a list of students
# Test URL: http://127.0.0.1:8000/students

@app.get("/students")
def get_students():
    data = [
        {"id": 1, "name": "Rahul"},
        {"id": 2, "name": "Priya"},
        {"id": 3, "name": "Amit"}
    ]
    return data


# GET Example 3 - Return ML model information
# This is how Streamlit checks which model is running before sending data
# Test URL: http://127.0.0.1:8000/model-info

@app.get("/model-info")
def model_info():
    return {
        "model": "Random Forest",
        "accuracy": 0.92,
        "status": "ready"
    }




# ==============================================================
# SECTION 2 - POST REQUEST
#
# POST is used to SEND data to the server.
# Data goes inside the request body as JSON.
# Server receives it, processes it, returns a response.
#
# Real world: Like filling a form and clicking Submit.
# You are sending data. Server does something with it.
#
# In ML projects: Streamlit sends patient data to FastAPI.
# FastAPI feeds it to the model. Model returns a prediction.
# ==============================================================


# POST Example 1 - Send a name, get a greeting back
# Test URL: http://127.0.0.1:8000/greet
# Body: {"name": "Rahul"}

class User(BaseModel):
    name: str

@app.post("/greet")
def greet(user: User):
    return {"msg": f"Hello {user.name}!"}


# POST Example 2 - Send two numbers, get the sum back
# Same flow as ML prediction. Input goes in, result comes out.
# Test URL: http://127.0.0.1:8000/add
# Body: {"a": 10, "b": 25}

class Nums(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(data: Nums):
    result = data.a + data.b
    return {"result": result}


# POST Example 3 - Disease prediction (actual ML pattern)
# This is exactly what your final project will look like.
# Right now it uses a simple rule instead of a real model.
# Later you will replace that one line with model.predict()
# Test URL: http://127.0.0.1:8000/predict
# Body: {"age": 55, "bp": 140, "cholesterol": 230}

class Patient(BaseModel):
    age: int
    bp: int
    cholesterol: int

@app.post("/predict")
def predict(p: Patient):
    # In your real project replace this line with:
    # result = model.predict([[p.age, p.bp, p.cholesterol]])[0]
    result = "High Risk" if p.age > 50 else "Low Risk"
    return {"prediction": result}




# ==============================================================
# SECTION 3 - PATH PARAMETERS
#
# Path parameters are dynamic values inside the URL itself.
# Used when you want to identify ONE specific resource.
#
# Real world: Your roll number in the URL.
# /student/101 means "give me data for student 101 only."
# ==============================================================


# PATH PARAM Example 1 - Get one student by ID
# Test URL: http://127.0.0.1:8000/student/101
# Test URL: http://127.0.0.1:8000/student/205
# Try this: http://127.0.0.1:8000/student/abc  (will give error, abc is not int)

@app.get("/student/{sid}")
def get_student(sid: int):
    return {"student_id": sid, "name": "Rahul"}


# PATH PARAM Example 2 - Get product by name
# Test URL: http://127.0.0.1:8000/product/laptop
# Test URL: http://127.0.0.1:8000/product/phone

@app.get("/product/{name}")
def get_product(name: str):
    return {"product": name, "price": 999}


# PATH PARAM Example 3 - Get ML model by version
# In production you may have v1, v2, v3 of your model deployed.
# The client picks which version to call using the path param.
# Test URL: http://127.0.0.1:8000/model/1
# Test URL: http://127.0.0.1:8000/model/2

@app.get("/model/{version}")
def get_model_version(version: int):
    return {
        "version": version,
        "type": "Random Forest",
        "accuracy": round(0.90 + (version * 0.01), 2)
    }




# ==============================================================
# SECTION 4 - QUERY PARAMETERS
#
# Query parameters come after ? in the URL.
# Used to filter or customize results.
# Usually optional. Have a default value.
#
# Real world: Filters on a shopping site.
# Same URL /products but ?brand=Apple shows only Apple products.
# ==============================================================


# QUERY PARAM Example 1 - Filter students by city
# city is not inside {} in the route so FastAPI treats it as query param
# Test URL: http://127.0.0.1:8000/filter-students?city=Mumbai
# Test URL: http://127.0.0.1:8000/filter-students?city=Pune

@app.get("/filter-students")
def filter_students(city: str):
    return {"city": city, "count": 25}


# QUERY PARAM Example 2 - Optional params with default values
# If you do not send the param, the default value is used automatically
# Test URL: http://127.0.0.1:8000/products
# Test URL: http://127.0.0.1:8000/products?brand=Apple
# Test URL: http://127.0.0.1:8000/products?brand=Apple&limit=5

@app.get("/products")
def get_products(brand: str = "all", limit: int = 10):
    return {"brand": brand, "limit": limit}


# QUERY PARAM Example 3 - Dataset filter (ML context)
# Streamlit uses this to fetch only the rows it needs from your dataset
# Test URL: http://127.0.0.1:8000/data
# Test URL: http://127.0.0.1:8000/data?label=diabetic
# Test URL: http://127.0.0.1:8000/data?label=diabetic&rows=50

@app.get("/data")
def get_data(label: str = "all", rows: int = 100):
    return {
        "label": label,
        "rows_fetched": rows,
        "source": "diabetes_dataset.csv"
    }
