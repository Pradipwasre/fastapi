# FastAPI Day 1 - Windows Setup and ML Project Guide

python -m venv venv
.\venv\Scripts\activate
pip install fastapi uvicorn
uvicorn api:app --reload

---

## PART 1 - Windows Setup

Copy and paste each command one by one into your VS Code terminal.

---

### Step 1 - Check Python is Installed

```
python --version
```

You should see something like `Python 3.10.x`. If you see an error, install Python from https://www.python.org/downloads/ and restart VS Code.

---

### Step 2 - Create a Project Folder

```
mkdir fastapi-day1
cd fastapi-day1
```

---

### Step 3 - Create Virtual Environment

```
python -m venv venv
```

---

### Step 4 - Activate Virtual Environment

```
venv\Scripts\activate
```

You will see `(venv)` at the start of your terminal line. This means the environment is active. Always activate before running any code.

---

### Step 5 - Install FastAPI and Uvicorn

```
pip install fastapi uvicorn
```

Wait for it to finish. You will see "Successfully installed" at the end.

---

### Step 6 - Create the API File

```
echo. > api.py
```

Now open `api.py` in VS Code and paste the code shared by your trainer.

---

### Step 7 - Run the Server

```
uvicorn api:app --reload
```

You will see this in the terminal:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Started reloader process
```

---

### Step 8 - Open in Browser

Copy this URL and open it in Chrome:

```
http://127.0.0.1:8000/docs
```

This is called Swagger UI. Every endpoint in your api.py will appear here. You can test all of them from this page.

---

### How to Stop the Server

```
Ctrl + C
```

---

### How to Start Again Next Time

Every time you open a new terminal session, run these two commands first:

```
cd fastapi-day1
venv\Scripts\activate
uvicorn api:app --reload
```

---

### Common Errors and Fixes

**Error: venv\Scripts\activate is not recognized**

Open PowerShell as Administrator and run:

```
Set-ExecutionPolicy RemoteSigned
```

Then try activating again.

**Error: ModuleNotFoundError: No module named 'fastapi'**

Virtual environment is not active. Run:

```
venv\Scripts\activate
```

Then run the server again.

**Error: address already in use**

Port 8000 is already being used by another server. Run on a different port:

```
uvicorn api:app --reload --port 8001
```

Then open `http://127.0.0.1:8001/docs` in the browser.

---
---

## PART 2 - How FastAPI Works in a Real Machine Learning Project

Read this after completing the hands-on code practice. This section explains why you are learning FastAPI and how every concept you practiced today fits into a real ML project.

---

### The Problem FastAPI Solves

You train a model in Jupyter Notebook. The model works perfectly. Accuracy is good. But right now only you can use it, because it lives inside a `.ipynb` file on your machine.

No one else can access it. No one can send their data to your model and get a prediction back.

FastAPI solves this. It wraps your model inside a server that anyone can talk to over the internet.

---

### The Complete Machine Learning Project Flow

```
1. Data Collection and Cleaning
   Jupyter Notebook
   pandas, numpy

2. Exploratory Data Analysis
   Jupyter Notebook
   matplotlib, seaborn

3. Model Training
   Jupyter Notebook
   scikit-learn, train_test_split, fit()

4. Save the Trained Model
   Jupyter Notebook
   pickle.dump(model, open("model.pkl", "wb"))

5. Build the API
   api.py using FastAPI
   Load model, create /predict endpoint

6. Build the Frontend
   app.py using Streamlit
   Take user input, call FastAPI, show result to user
```

Steps 1 to 4 you already know from your data science training.

Today you started Step 5.

Step 6 will come later in the course.

---

### How GET Works in an ML Project

GET is used to read information from the server without sending any data.

In an ML project you use GET for things like:

**Check if the server is running**

```python
@app.get("/")
def home():
    return {"status": "server is running"}
```

Streamlit calls this when it first loads to confirm the FastAPI server is up before showing the UI to the user.

**Get model information**

```python
@app.get("/model-info")
def model_info():
    return {
        "model": "Random Forest",
        "accuracy": 0.92,
        "features": ["age", "bp", "cholesterol"]
    }
```

Streamlit calls this to display model details on the dashboard page.

**Get list of available models**

```python
@app.get("/models")
def get_models():
    return ["Random Forest", "Logistic Regression", "XGBoost"]
```

Streamlit shows this as a dropdown. User selects which model to use for prediction.

GET endpoints do not accept any input data from the user. They only return information that is already on the server.

---

### How POST Works in an ML Project

POST is the most important endpoint in any ML deployment. This is where the actual prediction happens.

The user fills in their data on the Streamlit form. Streamlit sends that data to your FastAPI POST endpoint. FastAPI feeds it to the model. The model returns a prediction. FastAPI sends the prediction back to Streamlit. Streamlit shows it to the user.

**This is the POST endpoint you will write in your final project:**

```python
import pickle
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

model = pickle.load(open("model.pkl", "rb"))

class Patient(BaseModel):
    age: int
    bp: int
    cholesterol: int

@app.post("/predict")
def predict(p: Patient):
    features = [[p.age, p.bp, p.cholesterol]]
    result = model.predict(features)
    return {"prediction": str(result[0])}
```

The only difference between this and what you wrote today in practice is the `model.predict()` line. Everything else is identical.

You already know how to write this endpoint. You just need to load your pickle file on top.

---

### How Path Parameters Work in an ML Project

Path parameters identify one specific resource in the URL.

In an ML project you use path parameters when you have multiple models deployed and the user or Streamlit needs to pick one specific model.

**Example: Fetch a specific model version**

```python
@app.get("/model/{version}")
def get_model(version: int):
    model = pickle.load(open(f"model_v{version}.pkl", "rb"))
    return {"version": version, "loaded": True}
```

Streamlit calls `/model/1` or `/model/2` depending on which version the user selects.

**Example: Fetch prediction history for a specific patient**

```python
@app.get("/history/{patient_id}")
def get_history(patient_id: int):
    # fetch from database using patient_id
    return {"patient_id": patient_id, "past_predictions": [...]}
```

This is used in hospital or clinic applications where you want to look up a specific patient record by their ID.

Path parameters are mandatory. If the user does not provide them, the URL does not match any route and FastAPI returns a 404 error.

---

### How Query Parameters Work in an ML Project

Query parameters filter or customize results. They come after the question mark in the URL and are usually optional.

In an ML project you use query parameters when Streamlit needs to fetch a filtered version of data from your server.

**Example: Fetch dataset with filters**

```python
@app.get("/data")
def get_data(label: str = "all", rows: int = 100):
    df = pd.read_csv("diabetes.csv")
    if label != "all":
        df = df[df["label"] == label]
    return df.head(rows).to_dict(orient="records")
```

Streamlit calls `/data?label=diabetic&rows=50` to load only diabetic patients for display.

**Example: Filter predictions by confidence threshold**

```python
@app.get("/predictions")
def get_predictions(threshold: float = 0.5):
    # return only predictions where confidence is above threshold
    return {"threshold": threshold, "results": [...]}
```

Streamlit has a slider for confidence threshold. When the user moves the slider, Streamlit calls this endpoint with the new value.

Query parameters are optional because they have default values. If Streamlit does not send them, the server uses the defaults and still works correctly.

---

### Why FastAPI and Not Flask or Django

| | FastAPI | Flask | Django |
|--|---------|-------|--------|
| Speed | Very fast | Moderate | Moderate |
| Automatic Swagger docs | Yes, built-in | No | No |
| Data validation | Yes, automatic via Pydantic | Manual | Manual |
| Learning curve | Low | Low | High |
| Best for | ML APIs | Small apps | Full web apps |

FastAPI was built specifically for building APIs quickly. The automatic Swagger documentation at `/docs` means you do not need to write separate documentation or use Postman. Your docs are always up to date because they are generated directly from your code.

For a data scientist who wants to deploy an ML model with minimum extra work, FastAPI is the best choice.

---

### How FastAPI Connects with Streamlit

FastAPI and Streamlit are two separate Python processes running at the same time.

FastAPI runs on port 8000. Streamlit runs on port 8501. They talk to each other using HTTP requests.

```
User opens Streamlit app in browser
        |
        v
User fills in age, bp, cholesterol and clicks Predict
        |
        v
Streamlit sends a POST request to http://127.0.0.1:8000/predict
with the data as JSON in the request body
        |
        v
FastAPI receives the data
Feeds it to the loaded model
Gets the prediction back
Returns it as JSON to Streamlit
        |
        v
Streamlit receives the JSON response
Displays the prediction result to the user
```

**The Streamlit side looks like this:**

```python
import streamlit as st
import requests

st.title("Heart Disease Prediction")

age = st.number_input("Age")
bp = st.number_input("Blood Pressure")
cholesterol = st.number_input("Cholesterol")

if st.button("Predict"):
    data = {"age": age, "bp": bp, "cholesterol": cholesterol}
    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    result = response.json()
    st.write("Prediction:", result["prediction"])
```

Streamlit uses the `requests` library to call your FastAPI endpoint. The `json=data` part is exactly the request body that your POST endpoint receives.

This is the complete connection. Streamlit is the face. FastAPI is the brain. Your pickle model is the logic.

---

### Summary

| What You Learned | Where It Is Used in ML Project |
|-----------------|-------------------------------|
| GET request | Check server status, fetch model info, load dataset |
| POST request | Send user input to model, receive prediction |
| Path parameter | Select a specific model version or patient record |
| Query parameter | Filter dataset by label, rows, or threshold |
| BaseModel | Define what input data your model expects |
| Swagger at /docs | Test your API without building the frontend first |

You now have all the FastAPI knowledge needed to deploy your first ML model.
