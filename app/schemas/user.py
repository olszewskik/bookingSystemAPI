import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class Gender(str, Enum):
    male = "male"
    female = "female"


class UserBase(BaseModel):
    first_name: str
    last_name: str
    username: str
    gender: Gender = Field(None, alias="gender")
    phone: str = None
    email: str
    is_active: Optional[bool] = True
    is_admin: Optional[bool] = False


class UserCreate(UserBase):
    password: str

    class Config:
        orm_mode = True


class UserRead(UserBase):
    id: int
    creation_date: datetime.datetime

    class Config:
        orm_mode = True
