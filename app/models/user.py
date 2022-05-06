import pytz
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Boolean

from app.db.base import Base
from app.core.config import settings


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50), index=True, unique=True, nullable=False)
    gender = Column(String(10))
    phone = Column(String(10))
    email = Column(String(100), index=True, unique=True, nullable=False)
    password = Column(String(255))
    creation_date = Column(
        DateTime, default=datetime.now(pytz.timezone(settings.TIMEZONE))
    )
    is_active = Column(Boolean(), default=True)
    is_admin = Column(Boolean(), default=False)
