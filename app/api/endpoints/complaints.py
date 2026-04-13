
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas.complaints import ComplaintCreate, ComplaintUpdate, ComplaintResponse
from services.complaints_service import ComplaintService
from dependencies.db import get_db


router = APIRouter(prefix="/complaint", tags=["complaint"])
