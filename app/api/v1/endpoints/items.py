from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas, models
from app.api.deps import get_db, get_current_active_user, get_current_active_admin


router = APIRouter()


@router.get("/", response_model=List[schemas.ItemRead])
async def read_items(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user),
):
    items = await crud.item.get_items(db, skip=skip, limit=limit)
    return items


@router.post("/", response_model=schemas.ItemCreate)
async def create_item(
    item: schemas.ItemCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_admin),
):
    return await crud.item.create_item(db=db, item=item)


@router.get("/{item_id}", response_model=schemas.ItemRead)
async def read_item(
    item_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_active_user),
):
    db_item = await crud.item.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
