from fastapi import Depends, APIRouter, HTTPException, status, Request
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User
from app.schemas.users import UserCreate, UserOut, UserLogin
from app.security import hash_password, verify_password
from app.dependencies import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

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

@router.post("/login", response_model=UserOut)
def login(data: UserLogin, request: Request, db: Session =  Depends(get_db)):
    email = data.email.lower()

    user = db.scalar(select(User).where(User.email == email))
    if user is None or not verify_password(data.password, user.password_hash):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED,detail = "invalid email or password")

    request.session.clear()
    request.session["user_id"] = user.id
    return user 

@router.get("/me",response_model=UserOut)
def me(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/logout",status_code=status.HTTP_204_NO_CONTENT)
def logout(request: Request):
    request.session.clear()