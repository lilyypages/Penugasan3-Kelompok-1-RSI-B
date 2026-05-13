from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app.controllers.user_controller import router as user_router
from app.controllers.role_controller import router as role_router
from app.controllers.account_controller import router as account_router
from app.controllers.event_controller import router as event_router
from app.controllers.registration_controller import router as registration_router
from app.controllers import auth_controller
from app.database import Base, engine, SessionLocal
from app.models.role import Role

Base.metadata.create_all(bind=engine)

db = SessionLocal()
try:
    if not db.query(Role).first():
        db.add_all([Role(name="Admin"), Role(name="User")])
        db.commit()
        print("Seeder: Default roles created (Admin, User)")
finally:
    db.close()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router)
app.include_router(role_router)
app.include_router(account_router)
app.include_router(event_router)
app.include_router(registration_router)
app.include_router(auth_controller.router)