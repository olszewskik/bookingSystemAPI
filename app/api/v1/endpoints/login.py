from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.deps import get_db
from app.core.security import create_access_token
from app.core.config import settings

router = APIRouter()


@router.post("/login", response_model=schemas.Token, status_code=status.HTTP_200_OK)
def login_user(login: schemas.Login, db: Session = Depends(get_db)) -> Any:
    user = crud.user.authenticate(db, email=login.email, password=login.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
