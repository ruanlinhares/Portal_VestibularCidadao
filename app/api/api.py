from fastapi import APIRouter
from app.api.endpoints import Notas, User

api_router = APIRouter()
api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(notas.router, prefix="/notas", tags=["notas"])
