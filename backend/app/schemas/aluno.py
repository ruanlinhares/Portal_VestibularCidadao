from pydantic import BaseModel, EmailStr
from typing import Optional


class AlunoBase(BaseModel):
    alunoNome: str
    alunoEmail: EmailStr
    alunoTelefone: Optional[str] = None

class AlunoCreate(AlunoBase):
    pass

class AlunoUpdate(BaseModel):
    alunoNome: Optional[str] = None
    alunoEmail: Optional[EmailStr] = None
    alunoTelefone: Optional[str] = None

class AlunoRead(AlunoBase):
    id: int

    class Config:
        from_attributes = True
