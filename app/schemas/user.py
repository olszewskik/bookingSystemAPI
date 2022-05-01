import datetime
from enum import Enum
from pydantic import BaseModel, Field


class Gender(str, Enum):
    male = "male"
    female = "female"


class UserBase(BaseModel):
    first_name: str
    last_name: str
    gender: Gender = Field(None, alias="gender")
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
