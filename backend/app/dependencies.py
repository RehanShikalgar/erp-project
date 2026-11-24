from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import User

def get_current_user(request: Request, db: Session = Depends(get_db)):
    user_id = request.session.get("user_id")
    user = db.get(User, user_id) if user_id is not None else None
    
    if user is None:
        request.session.clear()
        raise HTTPException(status_code =  status.HTTP_401_UNAUTHORIZED, detail="Not Logged in")

    return user