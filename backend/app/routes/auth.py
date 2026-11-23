from fastapi import Depends, APIRouter, HTTPException, Status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas.users import UserCreate, UserOut
from app.security import hash_password

router = APIRouter(prefix="/auth", tags=[auth])

@router.post("/register", response_model= UserOut, status_code=status.HTTP_201_CREATED)
def register(data: UserCreate, db: Session = Depends(get_db)):
    email= data.email.lower()

    existing = db.scalar(select(User).where(User.email == email))

    if existing:
        raise HTTPException(status_code = status.HTTP_409_CONFLICT, detail="email already registered")

    user = User(name = data.name, email = email, password_hash = hash_password(data.password))

    db.add(user)
    db.commit()
    db.refresh(user)
    return user