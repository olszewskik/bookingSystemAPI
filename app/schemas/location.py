from pydantic import BaseModel


class LocationBase(BaseModel):
    name: str
    latitude: float = None
    longitude: float = None

    class Config:
        orm_mode = True


class LocationCreate(LocationBase):
    pass


class LocationRead(LocationBase):
    id: int

    class Config:
        orm_mode = True
