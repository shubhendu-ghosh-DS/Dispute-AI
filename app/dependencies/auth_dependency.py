from fastapi import Depends, HTTPException
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from core.config import settings
from dependencies.db import get_db
from repositories.user_repo import UserRepository
from fastapi.security import OAuth2PasswordBearer


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    user = UserRepository.get_user_by_email(db, email)
    if user is None:
        raise credentials_exception
    return user