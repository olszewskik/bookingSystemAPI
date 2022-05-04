from typing import Optional
from datetime import datetime

from sqlalchemy.orm import Session

from app.core.security import get_password_hash, verify_password
from app.models.user import User
from app.schemas.user import UserCreate


class CRUDUser:
    def get_user_by_id(self, db: Session, *, user_id: int) -> User:
        return db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, db: Session, *, email: str) -> Optional[User]:
        return db.query(User).filter(User.email == email).first()

    def get_users(self, db: Session, *, skip: int = 0, limit: int = 100) -> User:
        return db.query(User).offset(skip).limit(limit).all()

    def create_user(self, db: Session, *, user: UserCreate) -> User:
        new_user = User(
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

    def authenticate(self, db: Session, *, email: str, password: str) -> Optional[User]:
        user = self.get_user_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(password, user.password):
            return None
        return user

    def is_active(self, user: User) -> bool:
        return user.is_active


user = CRUDUser()
