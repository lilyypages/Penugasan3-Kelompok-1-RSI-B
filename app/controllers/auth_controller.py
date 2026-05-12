from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = auth_service.login(db, form_data.username, form_data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    return {
        "access_token": token,
        "token_type": "bearer"
    }