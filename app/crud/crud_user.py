from typing import Optional
from datetime import datetime

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app import models, schemas


class CRUDUser:
    async def get_user_by_id(self, db: Session, *, user_id: int) -> models.User:
        return db.query(models.User).filter(models.User.id == user_id).first()

    async def get_user_by_email(self, db: Session, *, email: str) -> Optional[models.User]:
        return db.query(models.User).filter(models.User.email == email).first()

    async def get_users(self, db: Session, *, skip: int = 0, limit: int = 100) -> models.User:
        return db.query(models.User).offset(skip).limit(limit).all()

    async def create_user(self, db: Session, *, user: schemas.UserCreate) -> models.User:
        new_user = models.User(
            first_name=user.first_name,
            last_name=user.last_name,
            gender=user.gender,
            phone=user.phone,
            email=user.email,
            status=user.status,
            password=get_password_hash(user.password),
            creation_date=datetime.now(),
        )
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user

    async def authenticate(self, db: Session, *, email: str, password: str) -> Optional[models.User]:
        db_user = await self.get_user_by_email(db, email=email)
        if not db_user:
            return None
        if not verify_password(password, db_user.password):
            return None
        return db_user

    def is_active(self, user: models.User) -> bool:
        return user.is_active


user = CRUDUser()
