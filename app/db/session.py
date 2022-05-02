from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.core.config import settings


engine = create_engine(
    f"mariadb+pymysql://{settings.DATABASE_USER}:{settings.DATABASE_PASS}@{settings.DATABASE_SERVER}/{settings.DATABASE_NAME}"
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
