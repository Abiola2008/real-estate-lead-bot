"""
Health check endpoints.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """
    Basic health check.
    Returns 200 if the API process is running.
    """
    return {"status": "ok"}
