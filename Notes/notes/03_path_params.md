# Path Parameters

## What are Path Parameters?

Path parameters are dynamic values placed inside the URL itself.

They are used to identify one specific resource.

---

## Real World Analogy

Your roll number in the URL.

`/student/101` means "give me information about student number 101 specifically."

The number 101 is the path parameter. It changes depending on which student you want.

---

## Syntax

```python
@app.get("/student/{sid}")
def get_student(sid: int):
    return {"id": sid}
```

The `{sid}` in the route and `sid` in the function parameter must have the same name.

FastAPI automatically:
- Extracts the value from the URL
- Converts it to the type you declared (`int`, `str`, etc.)
- Returns an error if the type is wrong

---

## Examples of Path Parameters in URLs

```
/student/101          sid = 101
/student/205          sid = 205
/product/laptop       name = "laptop"
/product/phone        name = "phone"
/model/3              version = 3
```

---

## Type Checking is Automatic

```python
@app.get("/student/{sid}")
def get_student(sid: int):
    ...
```

If someone calls `/student/abc`, FastAPI returns a 422 error automatically because "abc" cannot be converted to an integer.

You do not write any validation code. FastAPI handles it.

---

## Path Parameter vs Hardcoded Route

```python
# Hardcoded - only works for this exact URL
@app.get("/student/101")
def one_student():
    ...

# Path parameter - works for any student ID
@app.get("/student/{sid}")
def any_student(sid: int):
    ...
```

Always use path parameters when the value changes.

---

## Why Data Scientists Use Path Parameters

- Fetch a specific row from a dataset by index
- Load a specific model version
- Get results for a specific experiment ID
- Retrieve one prediction record by ID

---

## After Reading This

Open `code/03_path_params/main.py` and run the examples.

Test by changing the value in the URL and seeing the response change.
