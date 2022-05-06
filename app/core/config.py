import os
from dotenv import load_dotenv
from pydantic import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Booking System API"
    TIMEZONE: str = "Poland"
    DATABASE_SERVER: str = os.getenv("DB_SERVER")
    DATABASE_NAME: str = os.getenv("DB_NAME")
    DATABASE_USER: str = os.getenv("DB_USER")
    DATABASE_PASS: str = os.getenv("DB_PASS")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30


settings = Settings()
