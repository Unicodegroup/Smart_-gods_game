from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from core.config import settings

Base = declarative_base()

# Engine
engine = create_engine(settings.sqlalchemy_database_url)

# Session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Dependency (برای FastAPI اگه استفاده کردی)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
