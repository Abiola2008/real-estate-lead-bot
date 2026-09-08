# Frontend — React

Real Estate Lead Bot user interfaces.

## Structure

```text
frontend/
└── src/
    ├── components/
    │   ├── ui/           # Shared UI primitives
    │   ├── chat/         # Customer chat components
    │   ├── leads/        # Lead list / detail components
    │   ├── dashboard/    # Sales dashboard components
    │   └── followups/    # Follow-up components
    ├── pages/
    │   ├── customer/     # Public customer chat pages
    │   ├── auth/         # Login / auth pages
    │   └── dashboard/    # Internal sales pages
    ├── services/         # API client functions
    ├── hooks/            # Custom React hooks
    ├── types/            # TypeScript types
    ├── utils/            # Helpers
    └── app/              # App root, providers, router
```

## Local Development

```bash
npm install
npm run dev
```

## Next Steps

1. Set up Vite + React + TypeScript properly
2. Build the customer chat interface
3. Build the sales dashboard
