import datetime

from typing import Optional
from pydantic import BaseModel


class ItemBase(BaseModel):
    description: str


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int
    creation_date: datetime.datetime
    last_modified_date: Optional[datetime.datetime]

    class Config:
        orm_mode = True


class ItemUpdate(ItemBase):
    pass
