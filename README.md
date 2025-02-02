# FastAPI Admin Template

A modern FastAPI admin template with SQLModel and Starlette Admin.

## Prerequisites

- Python 3.11 or higher
- PostgreSQL
- UV package manager

## Setup

1. Install UV if you haven't already:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Create and activate a virtual environment:
```bash
uv venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate     # On Windows
```

3. Install dependencies:
```bash
uv pip install -e ".[dev]"
```

4. Copy `.env.example` to `.env` and configure your environment variables:
```bash
cp .env.example .env
```

5. Initialize the database:
```bash
alembic upgrade head
```

## Running the Application

Start the development server:
```bash
uvicorn app.main:app --reload
```

The admin interface will be available at `http://localhost:8000/admin`

## Development Scripts

- **Run Tests**: `pytest`
- **Lint Code**: `ruff check .`
- **Format Code**: `ruff format .`
- **Database Migrations**:
  - Create: `alembic revision --autogenerate -m "description"`
  - Apply: `alembic upgrade head`
  - Rollback: `alembic downgrade -1`

## Project Structure

```
fastapi-admin-template/
├── app/
│   ├── api/
│   ├── core/
│   ├── models/
│   └── main.py
├── alembic/
├── tests/
└── pyproject.toml
```
