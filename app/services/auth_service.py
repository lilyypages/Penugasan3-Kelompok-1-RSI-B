from sqlalchemy.orm import Session
from app.models.account import Account
from app.utils.security.hash import verify_password
from app.utils.security.jwt import create_access_token
from app.repositories import auth_repository

def login(db: Session, email: str, password: str):
    account = auth_repository.get_by_email(db, email)

    if not account:
        return None

    if not verify_password(password, account.password):
        return None

    token = create_access_token({
        "sub": account.email,
        "role": account.role_id
    })

    return token