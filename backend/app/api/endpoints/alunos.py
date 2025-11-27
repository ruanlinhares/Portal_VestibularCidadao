from fastapi import APIRouter, HTTPException
from typing import List

from backend.app.models import Aluno
from backend.app.schemas import AlunoCreate, AlunoRead, AlunoUpdate

router = APIRouter()

@router.post("/", response_model= AlunoRead, status_code=201)
async def criar_aluno(payload: AlunoCreate):
    aluno = await Aluno.create(**payload.model_dump())
    return await AlunoRead.model_validate(aluno)

@router.get("/", response_model=List[AlunoRead])
async def listar_aluno():
    alunos = await Aluno.all()
    return [await AlunoRead.model_validate(aluno) for aluno in alunos]

@router.get("/{aluno_id}", response_model=AlunoRead )
async def procurar_aluno(aluno_id: int):
    aluno = await Aluno.get_or_none(id=aluno_id)
    if not aluno:
        raise HTTPException(404, "Aluno nao encontrado")
    return await AlunoRead.model_validate(aluno)

@router.put("/{aluno_id}", response_model=AlunoRead )
async def atualizar_aluno(aluno_id: int, payload: AlunoUpdate):
    aluno = await Aluno.get_or_none(id=aluno_id)
    if not aluno:
        raise HTTPException(404, "Aluno nao encontrado")
    await aluno.update_from_dict(payload.model_dump(exclude_unset=True))
    await aluno.save()
    return await AlunoRead.model_validate(aluno)

@router.delete("/{aluno_id}", status_code=204)
async def remover_aluno(aluno_id:int):
    deleted = await Aluno.filter(id=aluno_id).delete()
    if not deleted:
        raise HTTPException(404, "Aluno nao encontrado")


