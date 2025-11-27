from fastapi import APIRouter, HTTPException
from typing import List

from backend.app.models import Professor
from backend.app.schemas import ProfessorCreate, ProfessorRead, ProfessorUpdate

router = APIRouter()

@router.post("/", response_model=ProfessorRead, status_code=201)
async def criar_professor(payload: ProfessorCreate):
    professor = await Professor.create(**payload.model_dump())
    return await ProfessorRead.model_validate(professor)

@router.get("/", response_model=List[ProfessorRead])
async def listar_professores():
    professores = await Professor.all()
    return [await ProfessorRead.model_validate(Professor) for Professor in professores]

@router.get("/{professor_id}", response_model=ProfessorRead)
async def procurar_professor(professor_id:int):
    professor = await Professor.get_or_none(id=professor_id)
    if not professor:
        raise HTTPException(404, "Professor nao encontrado")
    return await ProfessorRead.model_validate(professor)

@router.put("/{professor_id}", response_model=ProfessorRead)
async def atualizar_professor(professor_id:int, payload: ProfessorUpdate):
    professor = await Professor.get_or_none(id=professor_id)
    if not professor:
        raise HTTPException(404, "Professor nao encontrado")
    await professor.update_from_dict(payload.model_dump(exclude_unset=True))
    await professor.save()
    return await ProfessorRead.model_validate(professor)

@router.delete("/{professor_id}", status_code=204)
async def remover_professor(professor_id:int):
    deleted = await Professor.filter(id=professor_id).delete()
    if not deleted:
        raise HTTPException(404, "Professor nao encontrado")
