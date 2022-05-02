from sqlalchemy.orm import Session

from app.models.location import Location
from app.schemas.location import LocationBase


def get_location_by_id(db: Session, location_id: int):
    return db.query(Location).filter(Location.id == location_id).first()


def get_locations(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Location).offset(skip).limit(limit).all()


def create_location(db: Session, location: LocationBase):
    new_location = Location(
        name=location.name, latitude=location.latitude, longitude=location.longitude
    )
    db.add(new_location)
    db.commit()
    db.refresh(new_location)
    return new_location
