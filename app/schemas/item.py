from pydantic import BaseModel


class ItemBase(BaseModel):
    description: str


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
