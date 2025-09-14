"""Centralized configuration management using Pydantic Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


class DatabaseConfig(BaseAppSettings):
    """API keys configuration."""
    name: str = Field(None, alias="DATABASE_NAME")


class Settings(BaseAppSettings):
    """Main application settings."""
    database: DatabaseConfig = DatabaseConfig()


# Settings Singleton
settings = Settings()