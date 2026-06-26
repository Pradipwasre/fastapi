# GET Request

## What is GET?

GET is used to read or fetch data from the server.

It does NOT create, modify, or delete anything. It only reads.

---

## Real World Analogy

GET is like asking the librarian "show me the list of available books."

You are not adding or removing books. You are only asking to see something.

---

## How It Works

```
Client (Browser / Streamlit)
        |
        | GET /students
        v
FastAPI Server
        |
        | Returns JSON data
        v
Client receives the data
```

---

## Syntax

```python
@app.get("/your-route")
def function_name():
    return {"key": "value"}
```

The `@app.get(...)` decorator tells FastAPI:
- This function handles GET requests
- At this specific URL path

---

## What FastAPI Returns

FastAPI automatically converts Python dictionaries and lists to JSON.

You do not need to do any extra conversion.

```python
return {"name": "Rahul"}      # becomes   {"name": "Rahul"}
return [1, 2, 3]              # becomes   [1, 2, 3]
return {"students": [...]}    # becomes   {"students": [...]}
```

---

## Why Data Scientists Use GET

- Expose model metadata (name, version, accuracy)
- Return available datasets
- Check if the API server is running
- Fetch prediction history

---

## After Reading This

Open `code/01_get/main.py` and run the examples.

Test each endpoint in Swagger at `http://127.0.0.1:8000/docs`
