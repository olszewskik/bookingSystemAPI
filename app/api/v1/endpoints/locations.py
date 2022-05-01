from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api.deps import get_db
from app.crud import crud_location

from app import schemas

router = APIRouter()


@router.get("/{location_id}", response_model=schemas.LocationRead)
def read_location(location_id: int, db: Session = Depends(get_db)):
    db_location = crud_location.get_location_by_id(db, location_id=location_id)
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location


@router.get("/", response_model=List[schemas.LocationRead])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = crud_location.get_locations(db, skip=skip, limit=limit)
    return locations


@router.post("/", response_model=schemas.LocationBase)
def create_location(location: schemas.LocationBase, db: Session = Depends(get_db)):
    return crud_location.create_location(db=db, location=location)
