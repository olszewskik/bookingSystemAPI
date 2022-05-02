from typing import List, Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app import crud
from app import schemas

router = APIRouter()


@router.get(
    "/{user_id}", response_model=schemas.UserRead, status_code=status.HTTP_200_OK
)
def read_user(user_id: int, db: Session = Depends(get_db)) -> Any:
    db_user = crud.user.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
        )
    return db_user


@router.get("/", response_model=List[schemas.UserRead], status_code=status.HTTP_200_OK)
def read_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 100) -> Any:
    users = crud.user.get_users(db, skip=skip, limit=limit)
    return users


@router.post(
    "/", response_model=schemas.UserCreate, status_code=status.HTTP_201_CREATED
)
def create_user(user_in: schemas.UserCreate, db: Session = Depends(get_db)) -> Any:
    check_user = crud.user.get_user_by_email(db, email=user_in.email)
    if check_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this email already exist.",
        )
    new_user = crud.user.create_user(db=db, user=user_in)
    return new_user
