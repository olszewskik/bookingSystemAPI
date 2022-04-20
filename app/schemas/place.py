from pydantic import BaseModel


class PlaceBase(BaseModel):
    description: str


class Place(PlaceBase):
    id: int

    class Config:
        orm_mode = True
