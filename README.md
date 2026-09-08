# Real Estate Lead Bot

**PrimeHomes Realty** — An AI-powered real estate lead management system that receives customer enquiries, understands their requirements, qualifies leads, stores customer information, and helps the sales team follow up efficiently.

> **Status:** Foundation & scaffolding complete. Ready for Phase 1 implementation.

---

## Overview

A customer can send a natural-language message such as:

> "Hi, I'm looking for a 3-bedroom apartment around Lekki. My budget is around ₦80 million."

The system:

1. Receives the message
2. Understands the request (AI)
3. Extracts structured information
4. Asks for missing details when needed
5. Qualifies and scores the lead
6. Stores everything in PostgreSQL
7. Responds to the customer
8. Notifies the sales team for high-value (HOT) leads

---

## Architecture

```text
CUSTOMER
   ↓
REACT (Frontend)
   ↓
FASTAPI (Backend API + Business Logic)
   ↓
┌──────────────┬──────────────┐
│  PostgreSQL  │     n8n      │
│ (System of   │ (Workflows + │
│  Record)     │  Automation) │
└──────────────┴──────┬───────┘
                      │
         ┌────────────┼────────────┐
         ▼            ▼            ▼
        AI      Notifications  Google Sheets
```

### Technology Stack

| Layer          | Technology       | Responsibility                          |
|----------------|------------------|-----------------------------------------|
| Frontend       | React            | Customer chat + Sales dashboard         |
| Backend        | FastAPI / Python | API, validation, business rules, auth   |
| Automation     | n8n              | Workflows, AI calls, notifications      |
| Database       | PostgreSQL       | System of record                        |
| AI             | LLM              | Intent detection + entity extraction    |
| Reporting      | Google Sheets    | Secondary operational views             |

---

## Project Structure

```text
real-estate-lead-bot/
├── frontend/                 # React application
│   └── src/
│       ├── components/       # UI, chat, leads, dashboard, followups
│       ├── pages/            # customer, auth, dashboard
│       ├── services/
│       ├── hooks/
│       ├── types/
│       ├── utils/
│       └── app/
├── backend/                  # FastAPI application
│   └── app/
│       ├── api/v1/           # auth, leads, conversations, messages, followups, health
│       ├── models/
│       ├── schemas/
│       ├── services/
│       ├── repositories/
│       ├── core/             # config, security
│       └── db/
├── n8n/                      # Workflow definitions
│   └── workflows/
├── database/                 # Database-related assets
├── tests/                    # backend, frontend, e2e, ai
├── docs/                     # All project documentation
│   ├── OVERVIEW.md
│   ├── PRD.md
│   ├── architecture/
│   ├── database/
│   ├── api/
│   ├── automation/
│   ├── ai/
│   ├── frontend/
│   ├── development/
│   ├── qualification/
│   ├── testing/
│   └── deployment/
├── .env.example
├── .gitignore
├── docker-compose.yml
├── LICENSE
├── README.md
└── TASK.md                   # Development task tracker
```

---

## Documentation

All foundational documents live under `docs/`:

| Document | Location |
|----------|----------|
| Project Overview | `docs/OVERVIEW.md` |
| Product Requirements (PRD) | `docs/PRD.md` |
| System Architecture | `docs/architecture/SYSTEM_ARCHITECTURE.md` |
| Database Design | `docs/database/DATABASE_DESIGN.md` |
| API Specification | `docs/api/API_SPEC.md` |
| n8n Workflow Spec | `docs/automation/N8N_WORKFLOW_SPEC.md` |
| AI Specification | `docs/ai/AI_SPEC.md` |
| UI/UX Specification | `docs/frontend/UI_UX_SPEC.md` |
| Development Setup | `docs/development/DEVELOPMENT_SETUP.md` |
| Lead Qualification | `docs/qualification/LEAD_QUALIFICATION_SPEC.md` |
| Testing Spec | `docs/testing/TESTING_SPEC.md` |
| Deployment Spec | `docs/deployment/DEPLOYMENT_SPEC.md` |
| Task Tracker | `TASK.md` (root) |

**Always read the relevant documentation before implementing a feature.**

---

## Quick Start (Local Development)

### Prerequisites

- Docker & Docker Compose
- Node.js 20+
- Python 3.11+
- Git

### 1. Clone & configure

```bash
git clone https://github.com/Abiola2008/real-estate-lead-bot.git
cd real-estate-lead-bot
cp .env.example .env
# Edit .env with your values
```

### 2. Start infrastructure

```bash
docker compose up -d db n8n
```

### 3. Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
# Run migrations (once Alembic is set up)
# alembic upgrade head
uvicorn app.main:app --reload --port 8000
```

### 4. Frontend

```bash
cd frontend
npm install
npm run dev
```

Services will be available at:

- Frontend: http://localhost:3000 (or Vite default)
- Backend API: http://localhost:8000
- API docs: http://localhost:8000/docs
- n8n: http://localhost:5678
- PostgreSQL: localhost:5432

---

## Development Principles

1. **Keep it simple** — Use the simplest technology that correctly solves the problem.
2. **Clear responsibilities** — React = UI, FastAPI = business logic + API, n8n = workflows, PostgreSQL = source of truth, AI = language understanding.
3. **AI is not the source of truth** — Always validate AI output before writing to the database.
4. **Incremental development** — Build and test in small stages.
5. **Human-in-the-loop** — Support handoff to sales representatives.

See `docs/development/DEVELOPMENT_SETUP.md` and `TASK.md` for the full development roadmap.

---

## Current Phase

**Phase 1 — Foundation & Scaffolding** ✅ (this commit)

Next priorities (from `TASK.md`):

1. Backend FastAPI health endpoint + config
2. Database models + Alembic migrations
3. Core Lead / Conversation / Message APIs
4. Basic React customer chat interface
5. First n8n workflow (`PRH-LEAD-PROCESS-MESSAGE`)

---

## License

See [LICENSE](LICENSE).
