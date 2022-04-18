from fastapi import APIRouter

from app import schemas

router = APIRouter()


@router.get("/", response_model=schemas.User)
def read_users():
    return {"id": "1", "first_name": "Kamil", "last_name": "Olszewski"}
