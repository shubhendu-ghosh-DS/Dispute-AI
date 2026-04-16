from sqlalchemy.orm import Session
from models.complaint import Complaint

class ComplaintRepository:

    @staticmethod
    def create_complaint(db: Session, data: dict):
        complaint = Complaint(**data)
        db.add(complaint)
        db.commit()
        db.refresh(complaint)
        return complaint
    
    @staticmethod
    def get_complaint(db: Session, complaint_id: int):
        return db.query(Complaint).filter(Complaint.id == complaint_id).first()