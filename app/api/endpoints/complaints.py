
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.complaint import ComplaintCreate, ComplaintUpdate, ComplaintResponse
from services.complaint_service import ComplaintService
from dependencies.db import get_db
from dependencies.auth_dependency import get_current_user


router = APIRouter(prefix="/complaint", tags=["complaint"])



@router.post("/", response_model=ComplaintResponse, status_code=status.HTTP_201_CREATED)
def create_complaint(complaint: ComplaintCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    service = ComplaintService()
    created_complaint = service.create_complaint(db, user_id=user.id, data=complaint.dict())
    return created_complaint