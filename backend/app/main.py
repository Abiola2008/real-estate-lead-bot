"""
Real Estate Lead Bot — FastAPI application entry point.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.api.v1 import health

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
    description="PrimeHomes Realty — Real Estate Lead Bot API",
    docs_url="/docs",
    redoc_url="/redoc",
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health.router, prefix=settings.API_V1_PREFIX, tags=["health"])

# Future routers (uncomment as implemented):
# from app.api.v1 import auth, leads, conversations, messages, followups
# app.include_router(auth.router, prefix=settings.API_V1_PREFIX, tags=["auth"])
# app.include_router(leads.router, prefix=settings.API_V1_PREFIX, tags=["leads"])
# app.include_router(conversations.router, prefix=settings.API_V1_PREFIX, tags=["conversations"])
# app.include_router(messages.router, prefix=settings.API_V1_PREFIX, tags=["messages"])
# app.include_router(followups.router, prefix=settings.API_V1_PREFIX, tags=["follow-ups"])


@app.get("/")
async def root():
    return {
        "message": "Real Estate Lead Bot API",
        "docs": "/docs",
        "health": f"{settings.API_V1_PREFIX}/health",
    }
