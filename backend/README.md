# Backend (OpenIntel API)

This directory contains the **FastAPI backend** for OpenIntel.

## Tech Stack
- Python 3.11
- FastAPI
- Uvicorn
- Pytest
- Docker

---

## Running with Docker (Recommended)

From the **project root**:

```bash
docker compose up --build backend
```

Or from this directory:

```bash
docker build -t openintel-backend .
docker run -p 8000:8000 openintel-backend
```

The API will be available at:

```
http://localhost:8000
```

---

## API Endpoints

- `POST /ip`
- `POST /domain`

All requests expect JSON payloads.

---

## Running Tests (Pytest)

Tests live under the `tests/` directory.

### Run tests locally (without Docker)

```bash
pip install -r requirements.txt
pytest
```

### Run tests inside Docker

```bash
docker run --rm openintel-backend pytest
```

---

## Project Structure

```
app/
├── main.py
├── routers/
├── services/
├── utils/
tests/
```

---

## Notes
- DNS, SSL, and RDAP lookups are handled in `utils/`
- Business logic lives in `services/`
- Routes are defined in `routers/`
