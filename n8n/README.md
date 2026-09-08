# n8n Workflows

Automation and orchestration layer for the Real Estate Lead Bot.

## Recommended Workflows

| Workflow Name              | Purpose                                      |
|----------------------------|----------------------------------------------|
| PRH-LEAD-PROCESS-MESSAGE   | Main message processing + AI extraction      |
| PRH-LEAD-QUALIFY           | Lead scoring and classification              |
| PRH-LEAD-NOTIFY-SALES      | HOT lead notifications                       |
| PRH-FOLLOWUP-REMINDER      | Scheduled follow-up reminders                |
| PRH-SHEET-SYNC-LEAD        | Google Sheets synchronization                |
| PRH-ERROR-HANDLER          | Centralized error handling                   |

## Principles

- FastAPI owns application state and business rules.
- n8n owns workflow orchestration and external integrations.
- n8n should call FastAPI APIs rather than writing directly to the database.
- AI output must be validated before it becomes authoritative data.

See `docs/automation/N8N_WORKFLOW_SPEC.md` for full specifications.
