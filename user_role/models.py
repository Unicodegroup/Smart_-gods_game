from sqlalchemy import (
    Column,
    String,
    Text,
    Boolean,
    func,
    Integer,
    DateTime,
    ForeignKey,
    
)

from core.database import Base


class UserRole(Base):
    __tablename__ = "user_role"
    id = Column(Integer, primary_key=True, unique=True, autoincrement=True)
    username = Column(String(256), unique=True)
    
    created_date = Column(DateTime, server_default=func.now())
    updated_date = Column(
        DateTime, server_default=func.now(), server_onupdate=func.now()
    )
    role = Column(String(256))