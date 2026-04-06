from sqlalchemy.orm import Session
from repositories.user_repo import UserRepository
from core.security import verify_password, get_password_hash, create_access_token


class AuthService:
    @staticmethod
    def signup(db: Session, email: str, password: str):
        existing_user = UserRepository.get_user_by_email(db, email)
        if existing_user:
            raise ValueError("Email already registered")
        hashed_password = get_password_hash(password)
        user = UserRepository.create_user(db, email, hashed_password)

        token = create_access_token(data={"sub": user.email})
        return user, token
    
    @staticmethod
    def login(db: Session, email: str, password: str):
        user = UserRepository.get_user_by_email(db, email)
        if not user or not verify_password(password, user.hashed_password):
            raise ValueError("Invalid email or password")
        
        token = create_access_token(data={"sub": user.email})
        return user, token