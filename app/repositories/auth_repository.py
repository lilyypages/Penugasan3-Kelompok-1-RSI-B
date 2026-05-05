from sqlalchemy.orm import Session
from app.models.account import Account

def get_by_email(db: Session, email: str):
    return db.query(Account).filter(Account.email == email).first()

def create_account(db: Session, account):
    db.add(account)
    db.commit()
    db.refresh(account)
    return account
