import datetime

from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str
    gender: str
    phone: str
    email: str
    status: str


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserRead(UserBase):
    id: int
    creation_date: datetime.datetime

    class Config:
        orm_mode = True
