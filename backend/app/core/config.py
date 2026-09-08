"""
Application configuration loaded from environment variables.
"""

from functools import lru_cache
from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    APP_ENV: str = "development"
    APP_NAME: str = "real-estate-lead-bot"
    DEBUG: bool = True
    LOG_LEVEL: str = "INFO"

    # API
    API_V1_PREFIX: str = "/api/v1"
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:5173"]

    # Database
    DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/real_estate_leads"

    # Security
    JWT_SECRET: str = "change-me-to-a-long-random-secret-in-production"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60
    SERVICE_TOKEN: str = "change-me-service-to-service-token"

    # n8n
    N8N_WEBHOOK_URL: str = "http://localhost:5678/webhook/lead-process-message"
    N8N_WEBHOOK_SECRET: str = "change-me-n8n-webhook-secret"
    N8N_BASE_URL: str = "http://localhost:5678"

    # AI
    AI_PROVIDER: str = "openai"
    AI_API_KEY: str = ""
    AI_MODEL: str = "gpt-4o-mini"
    AI_TIMEOUT_SECONDS: int = 30


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
