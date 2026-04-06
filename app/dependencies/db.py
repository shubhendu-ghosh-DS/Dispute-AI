from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from core.config import settings

DATBASE_URL = settings.DATABASE_URL

engine = create_engine(DATBASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

#dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

        