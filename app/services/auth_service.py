from sqlalchemy.orm import Session
from sqlalchemy import or_
from app.models.account import Account
from app.utils.security.hash import verify_password
from app.utils.security.jwt_utils import create_access_token
from app.repositories import auth_repository
def login(db: Session, identifier: str, password: str):
    account = db.query(Account).filter(
        or_(Account.email == identifier, Account.username == identifier)
    ).first()
    if not account:
        return None
    if not verify_password(password, account.password):
        return None
    token = create_access_token({
        "sub": account.email,
        "role": account.role_id
    })
    return token