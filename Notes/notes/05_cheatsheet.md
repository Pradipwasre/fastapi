# FastAPI Day 1 - Quick Reference

---

## Run the Server

```bash
uvicorn main:app --reload
```

Open Swagger: `http://127.0.0.1:8000/docs`

---

## GET Request

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/route")
def function_name():
    return {"key": "value"}
```

Use when: Reading or fetching data. Nothing is created or changed.

---

## POST Request

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    field1: int
    field2: str

@app.post("/route")
def function_name(data: InputData):
    return {"result": data.field1}
```

Use when: Sending data to the server. Used in every ML prediction API.

---

## Path Parameter

```python
@app.get("/student/{sid}")
def get_student(sid: int):
    return {"id": sid}
```

Test: `GET /student/101`

Use when: Identifying one specific resource by ID or name.

---

## Query Parameter

```python
@app.get("/students")
def get_students(city: str = "all", limit: int = 10):
    return {"city": city, "limit": limit}
```

Test: `GET /students?city=Mumbai&limit=5`

Use when: Filtering or customizing results. Default value makes it optional.

---

## Combining Path and Query

```python
@app.get("/data/{dataset}")
def get_data(dataset: str, rows: int = 100):
    return {"dataset": dataset, "rows": rows}
```

Test: `GET /data/diabetes?rows=50`

---

## HTTP Methods Summary

| Method | Purpose | FastAPI Decorator |
|--------|---------|------------------|
| GET | Read data | `@app.get()` |
| POST | Send or create data | `@app.post()` |
| PUT | Update data | `@app.put()` |
| DELETE | Delete data | `@app.delete()` |

---

## ML Deployment Pattern (Coming Later)

```python
import pickle
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
model = pickle.load(open("model.pkl", "rb"))

class InputData(BaseModel):
    age: int
    bp: int
    cholesterol: int

@app.post("/predict")
def predict(data: InputData):
    features = [[data.age, data.bp, data.cholesterol]]
    result = model.predict(features)
    return {"prediction": str(result[0])}
```

This is the full pattern. Today you learned everything except loading the pickle file.

---

## Common Mistakes

**Wrong: Forgetting to activate venv**
```bash
# Always activate first
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac
```

**Wrong: Route and function param name mismatch**
```python
# Wrong
@app.get("/student/{student_id}")
def get(sid: int):    # sid does not match student_id

# Correct
@app.get("/student/{sid}")
def get(sid: int):    # names match
```

**Wrong: Using GET when sending data**
```python
# Use POST for sending data in the body
# Use GET only for reading
```
