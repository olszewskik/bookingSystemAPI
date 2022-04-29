import os

from pydantic import BaseSettings
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = 'Booking System API'
    DATABASE_SERVER: str = os.getenv('DB_SERVER')
    DATABASE_NAME: str = os.getenv('DB_NAME')
    DATABASE_USER: str = os.getenv('DB_USER')
    DATABASE_PASS: str = os.getenv('DB_PASS')


settings = Settings()
