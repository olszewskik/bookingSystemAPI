from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import schemas
from app.api.deps import get_db
from app.crud import crud_item


router = APIRouter()


@router.get("/{item_id}", response_model=schemas.ItemCreate)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = crud_item.get_item(db, item_id=item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item


@router.get("/", response_model=List[schemas.ItemCreate])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud_item.get_items(db, skip=skip, limit=limit)
    return items


@router.post("/", response_model=schemas.ItemCreate)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud_item.create_item(db=db, item=item)
