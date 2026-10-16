# Demo API

A small JSON API built with FastAPI.

## Endpoints

- `GET /health` — Returns `{"status": "ok"}`
- `POST /echo` — Accepts `{"message": "string"}` and returns `{"message": "string"}`

## Local Run

Install dependencies:

```
uv pip install fastapi uvicorn pytest httpx --python /app/.venv/bin/python3
```

Start the server:

```
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Tests

Run the test suite:

```
/app/.venv/bin/python3 -m pytest tests/ -v
```
