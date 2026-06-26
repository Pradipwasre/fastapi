# FastAPI Day 1 - Hands-on Practice

**Trainer:** Pradip Wasre  
**Batch:** Data Science and GenAI  
**Topic:** FastAPI fundamentals with code practice

---

## What You Will Learn Today

- What FastAPI is and why data scientists use it
- How to set up a FastAPI project from scratch
- GET request
- POST request
- Path Parameters
- Query Parameters

By the end of this session you will have a working API running on your local machine that follows the same pattern used in real ML model deployment.

---

## The Big Picture

This is the deployment flow you are working toward:

```
Train Model in Jupyter Notebook
        |
        v
Save model as .pkl file
        |
        v
Build FastAPI server (load model, create /predict endpoint)
        |
        v
Build Streamlit frontend (take user input, call FastAPI, show result)
```

Today you are learning Step 2. Everything else builds on this.

---

## Repository Structure

```
fastapi-day1/
|
|-- README.md                  <-- You are here
|
|-- setup/
|   |-- README.md              <-- Step by step environment setup
|   |-- requirements.txt       <-- All packages needed
|
|-- notes/
|   |-- 01_get.md              <-- GET request notes
|   |-- 02_post.md             <-- POST request notes
|   |-- 03_path_params.md      <-- Path parameter notes
|   |-- 04_query_params.md     <-- Query parameter notes
|   |-- 05_cheatsheet.md       <-- One page quick reference
|
|-- code/
|   |-- 01_get/
|   |   |-- main.py            <-- 3 GET examples
|   |
|   |-- 02_post/
|   |   |-- main.py            <-- 3 POST examples
|   |
|   |-- 03_path_params/
|   |   |-- main.py            <-- 3 Path param examples
|   |
|   |-- 04_query_params/
|   |   |-- main.py            <-- 3 Query param examples
|   |
|   |-- 05_combined/
|       |-- main.py            <-- All concepts in one file
```

---

## How to Use This Repo

1. Read `setup/README.md` first and get your environment ready
2. For each concept, read the note file inside `notes/` first
3. Then open the matching code file inside `code/`
4. Run it and test in Swagger at `http://127.0.0.1:8000/docs`
5. Try the practice tasks at the bottom of each code file

---

## Quick Start (After Setup)

```bash
cd code/01_get
uvicorn main:app --reload
```

Open browser at `http://127.0.0.1:8000/docs`

---

## Prerequisites

- Python 3.8 or above installed
- VS Code installed
- Basic Python knowledge (functions, dictionaries, lists)
