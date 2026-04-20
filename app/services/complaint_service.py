
from sqlalchemy.orm import Session
from repositories.complaint_repo import ComplaintRepository
from complaint_generator import generate_complaint


class ComplaintService:
  def __init__(self):
    pass


  def create_complaint(self, db: Session, user_id:int, data: dict):
    ai_text = generate_complaint(data['description'], data['tone'], data['format'])

    complaint_data = {
      "user_id": user_id,
      "description": data['description'],
      "generated_text": ai_text,
      "format": data['format'],
      "tone": data['tone'],
      "status": "generated"
    }

    created_complaint = ComplaintRepository.create_complaint(db, complaint_data)
    return created_complaint

