from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.auth import LoginRequest, TokenResponse
from app.services import auth_service

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login", response_model=TokenResponse)
def login(request: LoginRequest, db: Session = Depends(get_db)):
    token = auth_service.login(db, request.email, request.password)

    if not token:
        raise HTTPException(status_code=401, detail="Invalid email or password")

    return {
        "access_token": token,
        "token_type": "bearer"
    }