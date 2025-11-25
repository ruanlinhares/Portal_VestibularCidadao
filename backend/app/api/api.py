from fastapi import APIRouter
from app.api.endpoints import alunos, notas, professores 

api_router = APIRouter()
api_router.include_router(alunos.router, prefix="/aluno", tags=["aluno"])
api_router.include_router(alunos.router, prefix="/notas", tags=["notas"])
api_router.include_router(alunos.router, prefix="/professor", tags=["professor"])