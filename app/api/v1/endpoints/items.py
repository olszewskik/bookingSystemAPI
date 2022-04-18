from fastapi import APIRouter

import schemas

router = APIRouter()


@router.get("/", response_model=schemas.Item)
def read_items():
    return {"id": "1", "description": "Item No. 1"}
