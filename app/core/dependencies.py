from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils.security.jwt_utils import decode_token
from app.models.account import Account

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    email = payload.get("sub")
    account = db.query(Account).filter(Account.email == email).first()
    if not account:
        raise HTTPException(status_code=401, detail="User not found")
    return account

def require_admin(current_user = Depends(get_current_user)):
    if current_user.role_id != 1:
        raise HTTPException(status_code=403, detail="Admin only")
    return current_user

def require_user(current_user = Depends(get_current_user)):
    if current_user.role_id not in [1, 2]:
        raise HTTPException(status_code=403, detail="User only")
    return current_user