from sqlalchemy import Column, Integer, String

from app.db.base import Base


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
