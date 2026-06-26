# Environment Setup

Follow these steps before writing any code. Do this once.

---

## Step 1 - Install Python

Make sure Python 3.8 or above is installed.

Check your version:

```bash
python --version
```

On Mac you may need:

```bash
python3 --version
```

If Python is not installed, download it from https://www.python.org/downloads/

---

## Step 2 - Clone or Download This Repository

**Option A - Using Git**

```bash
git clone https://github.com/your-username/fastapi-day1.git
cd fastapi-day1
```

**Option B - Download ZIP**

Click the green "Code" button on GitHub and select "Download ZIP". Extract and open the folder in VS Code.

---

## Step 3 - Open in VS Code

Open VS Code. Go to File > Open Folder. Select the `fastapi-day1` folder.

Open the integrated terminal:
- Windows: `Ctrl + backtick`
- Mac: `Cmd + backtick`

---

## Step 4 - Create Virtual Environment

A virtual environment keeps your project packages separate from your system Python.

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac**

```bash
python3 -m venv venv
source venv/bin/activate
```

You will see `(venv)` appear at the start of your terminal line. That confirms it is active.

---

## Step 5 - Install Packages

```bash
pip install -r setup/requirements.txt
```

This installs FastAPI and Uvicorn together.

To verify installation worked:

```bash
pip show fastapi
pip show uvicorn
```

---

## Step 6 - Run Your First Server

```bash
cd code/01_get
uvicorn main:app --reload
```

You should see output like this in the terminal:

```
INFO:     Uvicorn running on http://127.0.0.1:8000
INFO:     Started reloader process
```

---

## Step 7 - Open in Browser

Open these URLs in Chrome or any browser:

| URL | What You See |
|-----|-------------|
| `http://127.0.0.1:8000` | Raw JSON response |
| `http://127.0.0.1:8000/docs` | Swagger UI (interactive testing) |
| `http://127.0.0.1:8000/redoc` | ReDoc documentation |

Swagger at `/docs` is where you will test all your code during class.

---

## How to Stop the Server

Press `Ctrl + C` in the terminal.

---

## How to Deactivate Virtual Environment

```bash
deactivate
```

---

## Common Errors and Fixes

**Error: `venv\Scripts\activate` is not recognized (Windows)**

Run this in PowerShell as Administrator:

```bash
Set-ExecutionPolicy RemoteSigned
```

Then try activating again.

**Error: `ModuleNotFoundError: No module named 'fastapi'`**

Your virtual environment is not active. Run the activate command again.

**Error: Port 8000 already in use**

Another server is running on 8000. Use a different port:

```bash
uvicorn main:app --reload --port 8001
```

**Error: `uvicorn` is not recognized**

Packages were not installed. Make sure venv is active, then run:

```bash
pip install -r setup/requirements.txt
```
