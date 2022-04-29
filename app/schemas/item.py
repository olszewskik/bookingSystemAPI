import datetime

from pydantic import BaseModel


class ItemBase(BaseModel):
    description: str


class ItemCreate(ItemBase):
    id: int
    creation_date: datetime.datetime

    class Config:
        orm_mode = True
