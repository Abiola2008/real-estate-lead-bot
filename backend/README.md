# Backend — FastAPI

Real Estate Lead Bot API.

## Structure

```text
backend/
├── app/
│   ├── main.py              # Application entry point
│   ├── api/v1/              # Versioned API routers
│   ├── models/              # SQLAlchemy models
│   ├── schemas/             # Pydantic schemas
│   ├── services/            # Business logic
│   ├── repositories/        # Data access layer
│   ├── core/                # Config, security, utilities
│   └── db/                  # Database session & base
├── tests/
├── requirements.txt
└── README.md
```

## Local Development

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

API docs: http://localhost:8000/docs

## Next Steps

1. Implement database models (see `docs/database/DATABASE_DESIGN.md`)
2. Set up Alembic migrations
3. Implement authentication
4. Implement Lead, Conversation, Message endpoints
