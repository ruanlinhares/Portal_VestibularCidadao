from fastapi import APIRouter
from app.api.endpoints import notas, user, ai
from app.api.endpoints import auth

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(notas.router, prefix="/notas", tags=["notas"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])