import datetime

from pydantic import BaseModel


class ItemBase(BaseModel):
    description: str


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    id: int
    creation_date: datetime.datetime

    class Config:
        orm_mode = True
