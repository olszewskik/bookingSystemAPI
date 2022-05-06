from sqlalchemy import Column, Integer, String, DateTime, Boolean

from app.db.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    username = Column(String(50))
    gender = Column(String(10))
    phone = Column(String(10))
    email = Column(String(100), index=True, unique=True, nullable=False)
    password = Column(String(255))
    status = Column(String(50))
    creation_date = Column(DateTime)
    is_active = Column(Boolean(), default=True)
