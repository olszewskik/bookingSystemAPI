from sqlalchemy import Column, Integer, String, DateTime

from app.db.base import Base
from app.utils.utils import utils


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String(50))
    creation_date = Column(DateTime, default=utils.get_current_datetime())
    last_modified_date = Column(DateTime, default=None)
