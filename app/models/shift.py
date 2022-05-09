from sqlalchemy import Column, Integer, DateTime, Boolean, ForeignKey, Time
from sqlalchemy.orm import relationship

from app.db.base import Base
from app.utils.utils import utils


class Shift(Base):
    __tablename__ = "shift"

    id = Column(Integer, primary_key=True, index=True)
    location_id = Column(Integer, ForeignKey("location.id"))
    day = Column(Integer)
    start_time = Column(Time)
    end_time = Column(Time)
    is_active = Column(Boolean(), default=True)

    location = relationship("Location", back_populates="shifts")
