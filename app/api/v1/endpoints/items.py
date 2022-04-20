from fastapi import APIRouter

from app import schemas

router = APIRouter()


@router.get("/", response_model=schemas.Item)
def read_items():
    return {"id": "1", "description": "Item No. 1"}
