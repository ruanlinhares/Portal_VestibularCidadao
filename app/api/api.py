from fastapi import APIRouter
from app.api.endpoints import notas, user, ai

api_router = APIRouter()

api_router.include_router(user.router, prefix="/user", tags=["user"])
api_router.include_router(notas.router, prefix="/notas", tags=["notas"])
api_router.include_router(ai.router, prefix="/ai", tags=["ai"])