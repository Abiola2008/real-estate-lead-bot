# Database

PostgreSQL is the system of record for the Real Estate Lead Bot.

## Core Entities (MVP)

- users
- roles
- leads
- conversations
- messages
- lead_scores
- lead_assignments
- follow_ups
- activities
- integration_syncs

Full schema definition: `docs/database/DATABASE_DESIGN.md`

Migrations are managed with Alembic inside the `backend/` package.
