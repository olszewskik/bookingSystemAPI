from sqlalchemy.orm import Session
from datetime import datetime

from app.models.item import Item
from app.schemas.item import ItemCreate


def get_item(db: Session, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first()


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Item).offset(skip).limit(limit).all()


def create_item(db: Session, item: ItemCreate):
    db_item = Item(description=item.description, creation_date=datetime.now())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
