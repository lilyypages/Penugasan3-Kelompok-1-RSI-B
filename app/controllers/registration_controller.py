from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.registration import RegistrationCreate, RegistrationResponse
from app.services import registration_service
from app.core.dependencies import get_current_user, require_user, require_admin

router = APIRouter(prefix="/registrations", tags=["Registrations"])

@router.get("/", response_model=list[RegistrationResponse])
def get_registrations(
    db: Session = Depends(get_db),
    current_user = Depends(require_user)
):
    return registration_service.get_registrations(db)

@router.post("/", response_model=RegistrationResponse)
def create_registration(data: RegistrationCreate, db: Session = Depends(get_db), current_user = Depends(require_user)):
    try:
        return registration_service.create_registration(db, data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete("/{reg_id}")
def delete_registration(reg_id: int, db: Session = Depends(get_db), current_user = Depends(require_admin)):
    try:
        registration_service.delete_registration(db, reg_id)
        return {"message": "Registration deleted"}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))


@router.get("/live-blog")
def get_live_blog(db: Session = Depends(get_db), current_user = Depends(require_admin)):
    try:
        return registration_service.get_live_blog(db)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))