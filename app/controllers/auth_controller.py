from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.database import get_db
from app.services import auth_service, user_service, account_service
from app.schemas.register_schema import RegisterRequest, RegisterResponse, LoginJsonRequest, LoginResponse
from app.models import Account, User

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    token = auth_service.login(db, form_data.username, form_data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    account = db.query(Account).filter(
        (Account.email == form_data.username) | (Account.username == form_data.username)
    ).first()
    user = db.query(User).filter(User.id == account.user_id).first() if account else None
    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.post("/login/json")
def login_json(data: LoginJsonRequest, db: Session = Depends(get_db)):
    token = auth_service.login(db, data.username, data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid email or password")
    account = db.query(Account).filter(
        (Account.email == data.username) | (Account.username == data.username)
    ).first()
    user = db.query(User).filter(User.id == account.user_id).first() if account else None
    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": account.id,
            "username": account.username,
            "email": account.email,
            "role": "admin" if account.role_id == 1 else "user",
            "user_id": user.id if user else None
        }
    }

@router.post("/register", response_model=RegisterResponse)
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    existing = db.query(Account).filter(
        (Account.email == data.email) | (Account.username == data.username)
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="Username atau email sudah digunakan")

    from app.schemas.user import UserCreate
    user_data = UserCreate(first_name=data.username, last_name="", whatsapp="")
    user = user_service.create_user(db, user_data)

    from app.schemas.account import AccountCreate
    from app.utils.security.hash import hash_password
    account = Account(
        user_id=user.id,
        role_id=2,
        email=data.email,
        username=data.username,
        password=hash_password(data.password)
    )
    db.add(account)
    db.commit()
    db.refresh(account)

    return {"message": "Registrasi berhasil"}