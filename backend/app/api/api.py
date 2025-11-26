from fastapi import APIRouter
from backend.app.api.endpoints import alunos

api_router = APIRouter()
api_router.include_router(alunos.router, prefix="/aluno", tags=["aluno"])
"""api_router.include_router(notas.router, prefix="/notas", tags=["notas"])"""
"""api_router.include_router(professores.router, prefix="/professor", tags=["professor"])"""