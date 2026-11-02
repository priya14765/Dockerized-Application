# Python Web Service (Windows)

A minimal FastAPI application with HTML welcome and health pages, plus a JSON
health check.
Run it directly with Python on Windows; Docker is not needed.

## Requirements

- Python 3.11 or newer
- `pip`
- The `python` command

## Set up and run (PowerShell)

Open PowerShell in the project directory. Create a virtual environment,
install the dependencies, and start the web server:

```powershell
python -m venv venv
venv\Scripts\Activate
pip install -r requirements.txt
python.exe -m pip install --upgrade pip
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

If PowerShell prevents activation due to its execution policy, allow scripts for
the current PowerShell window and activate again:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
venv\Scripts\Activate
```

The server runs in the foreground. Leave that PowerShell window open, then
open a second PowerShell window and test the endpoints:

```powershell
curl.exe http://127.0.0.1:8000/
curl.exe http://127.0.0.1:8000/health
curl.exe http://127.0.0.1:8000/api/health
```

Open the root address for the welcome webpage and `/health` for the health
dashboard. The dashboard displays the current status and the `healthy`,
`degraded`, and `unhealthy` categories. The JSON health endpoint is available at
`/api/health`:

```text
> curl.exe http://127.0.0.1:8000/
<!doctype html>
<html lang="en">
  ...
  <h1>Welcome to the Python web service</h1>
  ...
</html>

> curl.exe http://127.0.0.1:8000/api/health
{"status":"healthy"}
```

The API is available at `http://127.0.0.1:8000`. Stop the server by pressing
`Ctrl+C` in the window where Uvicorn is running.

## Endpoints

| Method | Path | Response |
| --- | --- | --- |
| `GET` | `/` | HTML welcome page |
| `GET` | `/health` | HTML health dashboard with all three health categories |
| `GET` | `/api/health` | `{"status":"healthy"}` |

Interactive API documentation is available at
[`http://127.0.0.1:8000/docs`](http://127.0.0.1:8000/docs) while the service is
running.

## Project layout

```text
.
├── app/
│   └── main.py
├── requirements.txt
└── README.md
```

The project also includes a `Dockerfile` and `.dockerignore`, but neither is
used in the Python-only setup above.
