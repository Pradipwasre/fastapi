# POST Request

## What is POST?

POST is used to send data to the server.

The client puts data in the request body as JSON. The server receives it, processes it, and returns a response.

---

## Real World Analogy

POST is like filling a form and clicking Submit.

You are sending information. The server does something with it and replies.

---

## How It Works

```
Client sends JSON in request body
        |
        | POST /predict
        | Body: {"age": 55, "bp": 140}
        v
FastAPI Server receives the data
        |
        | Processes it (runs model, does calculation)
        v
Returns result as JSON
```

---

## Key Concept: Pydantic BaseModel

Before writing a POST endpoint, you define a class that describes what data you expect.

```python
from pydantic import BaseModel

class Patient(BaseModel):
    age: int
    bp: int
```

FastAPI uses this to:
- Validate that the correct fields are sent
- Automatically convert types (string "55" becomes integer 55)
- Show the expected format in Swagger docs

If wrong data is sent, FastAPI returns a clear error automatically. You do not need to write validation code.

---

## Syntax

```python
class InputData(BaseModel):
    field1: type
    field2: type

@app.post("/your-route")
def function_name(data: InputData):
    # use data.field1, data.field2
    return {"result": something}
```

---

## Why Data Scientists Use POST

This is the most important endpoint in ML deployment.

```
Streamlit UI
    User fills in patient details
        |
        | POST /predict
        | {"age": 55, "bp": 140, "cholesterol": 230}
        v
FastAPI
    model.predict([[55, 140, 230]])
        |
        v
Returns {"prediction": "High Risk"}
        |
        v
Streamlit shows result to user
```

Every ML API you build will have at least one POST endpoint.

---

## After Reading This

Open `code/02_post/main.py` and run the examples.

Test in Swagger at `http://127.0.0.1:8000/docs`

Click on any POST endpoint, click "Try it out", fill in the JSON body, and click Execute.
