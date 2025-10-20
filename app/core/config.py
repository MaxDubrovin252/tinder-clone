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


class APIV1Settings(BaseModel):
    prefix: str = "/v1"
    auth_prefix: str = "/auth"


class ApiSettings(BaseModel):
    prefix: str = "/api"
    v1: APIV1Settings = APIV1Settings()

    @property
    def bearer_token_url(self):
        parts = (
            self.prefix,
            self.v1.prefix,
            self.v1.auth_prefix,
            "/login",
        )
        path = "".join(parts)
        return path.removeprefix("/")


class AccessToken(BaseModel):
    lifetime_seconds: int = 3600
    reset_password_key: str = os.getenv("RESET_PASSWORD_KEY")
    verification_key: str = os.getenv("VERIFICATION_KEY")


class Settings(BaseSettings):
    db: DBSettings = DBSettings()
    access_token: AccessToken = AccessToken()


settings = Settings()
