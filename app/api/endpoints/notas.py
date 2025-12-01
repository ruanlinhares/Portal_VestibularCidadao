
from fastapi import APIRouter, HTTPException
from typing import List
from app.models import Notas, User
from app.schemas import NotaCreate, NotaRead, NotaUpdate

router = APIRouter()

@router.post("/", response_model=NotaRead, status_code=201)
async def atribuir_nota(payload: NotaCreate):
    aluno = await Aluno.get_or_none(id=payload.alunoId)
    if not aluno:
        raise HTTPException(404, "Aluno nao encontrado")
    nota = await Notas.create(
        alunoId=payload.alunoId,
        alunoNota=payload.alunoNota
    )
    return await NotaRead.model_validate(nota)

@router.get("/", response_model=List[NotaRead])
async def listar_notas():
    notas = await Notas.all().prefetch_related("aluno")
    return [await NotaRead.model_validate(nota) for nota in notas]

@router.get("/{nota_id}", response_model=NotaRead)
async def procurar_nota(nota_id: int):
    nota = await Notas.get_or_none(id=nota_id)
    if not nota:
        raise HTTPException(404, "Nota nao encontrada")
    return await NotaRead.model_validate(nota)

@router.put("/{nota_id}", response_model=NotaRead)
async def atualizar_nota(nota_id:int, payload: NotaUpdate):
    nota = await Notas.get_or_none(id=nota_id)
    if not nota:
        raise HTTPException(404, "Nota nao encontrada")
    await nota.update_from_dict(payload.model_dump(exclude_unset=True))
    await nota.save()
    return await NotaRead.model_validate(nota)

@router.delete("/{nota_id}", status_code=204)
async def apagar_nota(nota_id:int):
    deleted = await Notas.filter(id=nota_id).delete()
    if not deleted:
        raise HTTPException(404, "Nota nao encontrada")

