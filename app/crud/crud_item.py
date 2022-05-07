from sqlalchemy.orm import Session
from datetime import datetime

from app.models.item import Item
from app.schemas.item import ItemCreate


class CRUDItem:
    async def get_item(self, db: Session, *, item_id: int):
        return db.query(Item).filter(Item.id == item_id).first()

    async def get_items(self, db: Session, *, skip: int = 0, limit: int = 100):
        return db.query(Item).offset(skip).limit(limit).all()

    async def create_item(self, db: Session, *, item: ItemCreate):
        db_item = Item(description=item.description, creation_date=datetime.now())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    async def update_item(self, db: Session, *, item_id: int):
        pass

    async def remove_item(self, db: Session, *, item_id: int):
        db_item = db.query(Item).get(item_id)
        db.delete(db_item)
        db.commit()
        return db_item


item = CRUDItem()
