from sqlalchemy import Column, Integer, String, DateTime
from dependencies.db import Base

class Complaint(Base):
    __tablename__ = "complaints"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)
    
    title = Column(String, index=True)
    description = Column(String)

    generated_text = Column(String)
    format = Column(String)
    tone = Column(String)

    status = Column(String, default="open")

    created_at = Column(DateTime)
    updated_at = Column(DateTime)