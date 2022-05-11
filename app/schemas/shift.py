import datetime

from typing import List, Optional
from pydantic import BaseModel
from app.schemas.location import LocationBase


class Shift(BaseModel):
    location_id: int
    day: int
    start_time: datetime.time
    end_time: datetime.time
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True


class ShiftRead(Shift):
    id: int
    location: List[LocationBase] = []

    class Config:
        orm_mode = True
