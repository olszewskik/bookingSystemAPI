from pydantic import BaseModel


class GroupBase(BaseModel):
    description: str


class Group(GroupBase):
    id: int

    class Config:
        orm_mode = True
