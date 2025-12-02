from fastapi import APIRouter, HTTPException
from typing import List
from app.models import User
from app.schemas.User import CreateUserDTO, ListUserDTO, UpdateUserDTO

router = APIRouter()

@router.post("/inserir", response_model= ListUserDTO, status_code=201)
async def criar_user(payload: CreateUserDTO):
    
    existing = await User.filter(userEmail=payload.userEmail).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    hashed_password = User.hash_password(payload.userPassword)

    user = await User.create(
        userName=payload.userName,
        userEmail=payload.userEmail,
        userPhone=payload.userPhone,
        userPassword=hashed_password,
    )

    return ListUserDTO.from_orm(user)

@router.get("/listar", response_model=List[ListUserDTO])
async def list_user():
    users = await User.all()
    return [await ListUserDTO.model_validate(users) for user in users]

@router.get("/listar/{user_id}", response_model=ListUserDTO )
async def search_user(user_id: int):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(404, "Aluno nao encontrado")
    return await ListUserDTO.model_validate(user)

@router.put("/update/{user_id}", response_model=ListUserDTO )
async def update_user(user_id: int, payload: UpdateUserDTO):
    user = await User.get_or_none(id=user_id)
    if not user:
        raise HTTPException(404, "Aluno nao encontrado")
    await user.update_from_dict(payload.model_dump(exclude_unset=True))
    await user.save()
    return await ListUserDTO.model_validate(user)

@router.delete("/delete/{user_id}", status_code=204)
async def delete_user(user_id:int):
    userDelete = await User.filter(id=user_id).delete()
    if not userDelete:
        raise HTTPException(404, "Aluno nao encontrado")
