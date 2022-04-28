from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: str
    last_name: str


class UserCreate(UserBase):
    id: int

    class Config:
        orm_mode = True
