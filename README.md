# FinInfocom Task — Orders API

Lightweight Python service to manage orders, items and payments. Aggregation logic for combined order responses is implemented in `crud.fetch_all_orders`.

## Repository layout

- .env — environment variables (DB connection)
- crud.py — data access and aggregation helpers
- database.py — DB connection and session setup
- main.py — application entrypoint
- models.py — SQLAlchemy models
- schemas.py — Pydantic schemas
- routers/orders.py — API routes for orders
- utils.py — helper utilities
- requirements.txt — Python dependencies

## Requirements

- Python 3.9+
- A running database (configured via `.env`)

## Setup (create & activate virtual environment)

POSIX / macOS / WSL:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows PowerShell:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

Windows CMD:
```bat
python -m venv .venv
.\.venv\Scripts\activate.bat
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project root and add DB connection variables expected by `database.py`. Example (replace values):
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
```

## Running

Start the application:
```bash
python main.py
```
Check the routes defined in `routers/orders.py` for endpoints. Aggregated order responses are produced by `crud.fetch_all_orders`.

## Development

- Tests: add and run tests with your preferred framework (pytest recommended).
- Linting/formatting: run `flake8`/`black` (if configured in project).
- If you modify models in `models.py`, update queries in `crud.py` and schemas in `schemas.py`.

## Troubleshooting

- Ensure DB credentials in `.env` are correct and the DB is reachable.
- Inspect application output/logs from `main.py` for errors.

## Contributing

- Open issues or PRs with clear descriptions and tests for changes.
- Keep changes small and add or update unit tests where applicable.

## License

Specify project license here.