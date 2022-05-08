from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app import crud, schemas
from app.api.deps import get_db


router = APIRouter()


@router.get("/", response_model=List[schemas.ItemRead], status_code=status.HTTP_200_OK)
async def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = await crud.item.get_items(db, skip=skip, limit=limit)
    return items


@router.post("/", response_model=schemas.ItemRead, status_code=status.HTTP_201_CREATED)
async def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return await crud.item.create_item(db=db, item=item)


@router.get(
    "/{item_id}", response_model=schemas.ItemRead, status_code=status.HTTP_200_OK
)
async def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = await crud.item.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.put(
    "/{item_id}", response_model=schemas.ItemRead, status_code=status.HTTP_200_OK
)
async def update_item(
    item_id: int, item: schemas.ItemRead, db: Session = Depends(get_db)
):
    db_item = await crud.item.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return await crud.item.update_item(db=db, item_id=item_id, request=item)


@router.delete(
    "/{item_id}", response_model=schemas.ItemRead, status_code=status.HTTP_200_OK
)
async def delete_item(item_id: int, db: Session = Depends(get_db)):
    db_item = await crud.item.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item = await crud.item.remove_item(db=db, item_id=item_id)
    return db_item
