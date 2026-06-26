# Query Parameters

## What are Query Parameters?

Query parameters are values added after `?` in the URL.

They are used to filter, search, or customize the results without changing the main route.

---

## Real World Analogy

Filters on a shopping website.

You go to `/products` but you filter by brand, price range, or rating using query params.

Same route, different results based on what you filter.

---

## Syntax in the URL

```
/students?city=Mumbai
/students?city=Mumbai&age=21
/products?brand=Apple&limit=5
```

The `?` separates the route from the query params.

`&` separates multiple query params.

---

## Syntax in FastAPI

Query parameters are just regular function parameters that are NOT in curly braces in the route.

```python
@app.get("/students")
def get_students(city: str):
    return {"city": city}
```

FastAPI sees that `city` is not in the route path, so it automatically treats it as a query parameter.

---

## Optional Query Parameters

Add a default value to make it optional.

```python
@app.get("/students")
def get_students(city: str = "all"):
    return {"city": city}
```

Now both of these work:

```
/students              city = "all"   (uses default)
/students?city=Pune    city = "Pune"  (uses provided value)
```

---

## Multiple Query Parameters

```python
@app.get("/products")
def get_products(brand: str = "all", limit: int = 10):
    return {"brand": brand, "limit": limit}
```

All of these work:

```
/products
/products?brand=Apple
/products?limit=5
/products?brand=Apple&limit=5
```

---

## Path Parameter vs Query Parameter

| Feature | Path Parameter | Query Parameter |
|---------|---------------|----------------|
| Position | Inside the URL path | After ? in the URL |
| Purpose | Identify one resource | Filter or customize results |
| Example | `/student/101` | `/students?city=Mumbai` |
| Required | Usually yes | Usually no (has default) |
| Syntax | `{param}` in route | Regular function param |

---

## Why Data Scientists Use Query Parameters

- Filter a dataset by label, category, or column value
- Set the number of rows to return
- Pass a threshold for predictions
- Filter by date range

---

## After Reading This

Open `code/04_query_params/main.py` and run the examples.

Test the same URL with and without query params in Swagger to see the difference.
