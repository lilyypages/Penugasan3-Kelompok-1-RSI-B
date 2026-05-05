from sqlalchemy.orm import Session
from app.models import Account
from app.repositories import user_repository, role_repository
from app.utils.security.hash import hash_password

def get_accounts(db: Session):
    return db.query(Account).all()

def get_account(db: Session, account_id: int):
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise Exception("Account not found")
    return account

def create_account(db: Session, data):
    user = user_repository.get_by_id(db, data.user_id)
    if not user:
        raise Exception("User not found")

    role = role_repository.get_by_id(db, data.role_id)
    if not role:
        raise Exception("Role not found")

    account = Account(
        user_id=user.id,
        role_id=role.id,
        email=data.email,
        username=data.username,
        password=hash_password(data.password)  # Hash the password before storing
    )

    db.add(account)
    db.commit()
    db.refresh(account)
    return account

def update_account(db: Session, account_id: int, data):
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise Exception("Account not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(account, key, value)

    db.commit()
    db.refresh(account)
    return account

def delete_account(db: Session, account_id: int):
    account = db.query(Account).filter(Account.id == account_id).first()
    if not account:
        raise Exception("Account not found")
    db.delete(account)
    db.commit()