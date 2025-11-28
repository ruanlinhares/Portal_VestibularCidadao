from fastapi import APIRouter, HTTPException
from typing import List

from app.models import User
from app.schemas.User import CreateUserDTO, ListUserDTO, UpdateUserDTO

router = APIRouter()

@router.post("/inserir", response_model= AlunoRead, status_code=201)
async def criar_user(payload: CreateUserDTO):
    aluno = await Aluno.create(**payload.model_dump())
    return await AlunoRead.model_validate(aluno)

@router.get("/listar", response_model=List[ListUserDTO])
async def list_user():
    alunos = await Aluno.all()
    return [await AlunoRead.model_validate(aluno) for aluno in alunos]

@router.get("/listar/{aluno_id}", response_model=AlunoRead )
async def search_user(user_id: int):
    aluno = await Aluno.get_or_none(id=aluno_id)
    if not aluno:
        raise HTTPException(404, "Aluno nao encontrado")
    return await AlunoRead.model_validate(aluno)

@router.put("/update/{aluno_id}", response_model=AlunoRead )
async def update_user(user_id: int, payload: UpdateUserDTO):
    aluno = await Aluno.get_or_none(id=aluno_id)
    if not aluno:
        raise HTTPException(404, "Aluno nao encontrado")
    await aluno.update_from_dict(payload.model_dump(exclude_unset=True))
    await aluno.save()
    return await AlunoRead.model_validate(aluno)

@router.delete("/delete/{aluno_id}", status_code=204)
async def delete_user(user_id:int):
    deleted = await Aluno.filter(id=aluno_id).delete()
    if not deleted:
        raise HTTPException(404, "Aluno nao encontrado")
