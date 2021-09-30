import os
import secrets
from typing import List
from pydantic import AnyHttpUrl, BaseSettings
from dotenv import load_dotenv

load_dotenv()



class Settings(BaseSettings):
    API_V1_STR: str = "/api-v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    PROJECT_NAME: str = "Youtube Download Videos"

    class Config:
        case_sensitive = True


settings = Settings()