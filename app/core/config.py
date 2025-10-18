from pydantic_settings import BaseSettings
from pydantic import BaseModel
from dotenv import load_dotenv
import logging
import os

logging.info("Loading environment variables from .env file")


load_dotenv()

class DBSettings(BaseModel):
    url:str = os.getenv("DB_URL")
    echo:bool = False
    max_overflow : int = 5
    
    
    
class Settings(BaseSettings):
    db:DBSettings = DBSettings()



settings = Settings()

