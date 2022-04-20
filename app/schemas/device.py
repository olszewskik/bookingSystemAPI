from pydantic import BaseModel


class DeviceBase(BaseModel):
    description: str


class Device(DeviceBase):
    id: int

    class Config:
        orm_mode = True
