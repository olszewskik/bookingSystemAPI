from sqlalchemy.orm import Session

from app import models, schemas
from app.utils.utils import utils


class CRUDItem:
    async def get_item(self, db: Session, *, item_id: int):
        return db.query(models.Item).filter(models.Item.id == item_id).first()

    async def get_items(self, db: Session, *, skip: int = 0, limit: int = 100):
        return db.query(models.Item).offset(skip).limit(limit).all()

    async def create_item(self, db: Session, *, item: schemas.ItemCreate):
        db_item = models.Item(description=item.description)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    async def update_item(
        self, db: Session, *, item_id: int, request: schemas.ItemUpdate
    ):
        db_item = await self.get_item(db=db, item_id=item_id)
        for key, value in request:
            setattr(db_item, key, value)
        db_item.last_modified_date = utils.get_current_datetime()
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    async def remove_item(self, db: Session, *, item_id: int):
        db_item = db.query(models.Item).get(item_id)
        db.delete(db_item)
        db.commit()
        return db_item


item = CRUDItem()
