from pydantic import BaseModel


class ItemBase(BaseModel):
    description: str


class ItemCreate(ItemBase):
    id: int

    class Config:
        orm_mode = True
