from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool = False
    SECRET_KEY: str = "your-secret-key-here"

    class Config:
        env_file = ".env"

settings = Settings()
