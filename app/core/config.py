from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import logging
import os

logging.info("Loading environment variables from .env file")


load_dotenv()


class DBSettings(BaseModel):
    url: str = os.getenv("DB_URL")
    echo: bool = False
    max_overflow: int = 5


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_key: str = os.getenv("RESET_PASSWORD_KEY")
    verification_key: str = os.getenv("VERIFICATION_KEY")


class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    access_token: AccessToken = AccessToken()


settings = Settings()
