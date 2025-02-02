from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    DEBUG: bool
    SECRET_KEY: str = "your-secret-key-here"
    AUTH0_CLIENT_ID: str
    AUTH0_CLIENT_SECRET: str
    AUTH0_DOMAIN: str

    class Config:
        env_file = ".env"


settings = Settings() # type: ignore
