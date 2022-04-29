from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    # new_user = User(
    #     first_name=user.first_name,
    #     last_name=user.last_name,
    #     email=user.email,
    #     password=user.password,
    # )
    new_user_data = jsonable_encoder(user)
    new_user = User(**new_user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
