from sqlalchemy.orm import Session

from app import models, schemas


class CRUDShift:
    def get_shift_by_id(self, db: Session, shift_id: int):
        return db.query(models.Shift).filter(models.Shift.id == shift_id).first()

    def get_shifts(self, db: Session, skip: int = 0, limit: int = 100):
        return db.query(models.Shift).offset(skip).limit(limit).all()

    def create_shift(self, db: Session, shift: schemas.Shift):
        new_shift = models.Shift(
            location_id=shift.location_id,
            day=shift.day,
            start_time=shift.start_time,
            end_time=shift.end_time,
        )
        db.add(new_shift)
        db.commit()
        db.refresh(new_shift)
        return new_shift


shift = CRUDShift()
