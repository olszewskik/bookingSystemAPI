from app.db.session import SessionLocal, engine
from app.db.base import Base

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

