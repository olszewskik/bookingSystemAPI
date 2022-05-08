import pytz
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime

from app.db.base import Base
from app.core.config import settings


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(50))
    creation_date = Column(
        DateTime, default=datetime.now(pytz.timezone(settings.TIMEZONE))
    )
    last_modified_date = Column(DateTime, default=None)
