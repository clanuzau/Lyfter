# Lyfter Python Workspace

This repository is configured for writing and running Python programs in VS Code.

## Setup

Create and activate the local virtual environment:

```powershell
python -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Install runtime packages later by adding them to `requirements.txt`, then run:

```powershell
python -m pip install -r requirements.txt
```

## Run

Run the current Python file from VS Code with the task `Run current Python file`, or run this program directly:

```powershell
python helloworld.py
```

## Test

Place tests in a `tests` folder and run:

```powershell
python -m pytest
```
