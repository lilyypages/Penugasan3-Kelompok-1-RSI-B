from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.role import RoleCreate, RoleUpdate, RoleResponse
from app.services import role_service
from app.core.dependencies import get_current_user

router = APIRouter(prefix="/roles", tags=["Roles"])

@router.get("/", response_model=list[RoleResponse], summary="Get all roles")
def get_roles(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return role_service.get_roles(db)

@router.get("/{role_id}", response_model=RoleResponse, summary="Get roles by ID")
def get_role(role_id: int, db: Session = Depends(get_db)):
    try:
        return role_service.get_role(db, role_id)
    except Exception:
        raise HTTPException(status_code=404, detail="Role not found")

@router.post("/", response_model=RoleResponse, summary="Create new role")
def create_role(data: RoleCreate, db: Session = Depends(get_db)):
    return role_service.create_role(db, data)

@router.put("/{role_id}", response_model=RoleResponse, summary="Update role")
def update_role(role_id: int, data: RoleUpdate, db: Session = Depends(get_db)):
    try:
        return role_service.update_role(db, role_id, data)
    except Exception:
        raise HTTPException(status_code=404, detail="Role not found")

@router.delete("/{role_id}", summary="Delete role")
def delete_role(role_id: int, db: Session = Depends(get_db)):
    try:
        role_service.delete_role(db, role_id)
        return {"message": "Role deleted"}
    except Exception:
        raise HTTPException(status_code=404, detail="Role not found")
    
@router.patch("/{role_id}", response_model=RoleResponse, summary="Partially update role")
def patch_role(role_id: int, data: RoleUpdate, db: Session = Depends(get_db)):
    try:
        return role_service.update_role(db, role_id, data)
    except Exception:
        raise HTTPException(status_code=404, detail="Role not found")