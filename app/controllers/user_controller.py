from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate, UserUpdate, UserResponse
from app.services import user_service
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/", response_model=list[UserResponse], summary="Get all users")
def get_users(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return user_service.get_users(db)

@router.get("/{user_id}", response_model=UserResponse, summary="Get user by ID")
def get_user(user_id: int, db: Session = Depends(get_db)):
    try:
        return user_service.get_user(db, user_id)
    except Exception:
        raise HTTPException(status_code=404, detail="User not found")

@router.post("/", response_model=UserResponse, summary="Create new user")
def create_user(data: UserCreate, db: Session = Depends(get_db)):
    return user_service.create_user(db, data)

@router.put("/{user_id}", response_model=UserResponse, summary="Update user")
def update_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    try:
        return user_service.update_user(db, user_id, data)
    except Exception:
        raise HTTPException(status_code=404, detail="User not found")

@router.delete("/{user_id}", summary="Delete user")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user_service.delete_user(db, user_id)
        return {"message": "User deleted"}
    except Exception:
        raise HTTPException(status_code=404, detail="User not found")
    
@router.patch("/{user_id}", response_model=UserResponse, summary="Partially update user")
def patch_user(user_id: int, data: UserUpdate, db: Session = Depends(get_db)):
    try:
        return user_service.update_user(db, user_id, data)
    except Exception:
        raise HTTPException(status_code=404, detail="User not found")