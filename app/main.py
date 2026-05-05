from fastapi import FastAPI
from app.controllers.user_controller import router as user_router
from app.controllers.role_controller import router as role_router
from app.controllers.account_controller import router as account_router
from app.controllers.event_controller import router as event_router
from app.controllers.registration_controller import router as registration_router
from app.controllers import auth_controller

app = FastAPI()

app.include_router(user_router)
app.include_router(role_router)
app.include_router(account_router)
app.include_router(event_router)
app.include_router(registration_router)
app.include_router(auth_controller.router)