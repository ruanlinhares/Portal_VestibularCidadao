from pydantic import BaseModel, EmailStr
from typing import Optional



class ProfessorBase(BaseModel):
    professorNome: str
    professorEmail: EmailStr
    professorTelefone: Optional[str] = None

class ProfessorCreate(ProfessorBase):
    pass

class ProfessorUpdate(BaseModel):
    professorNome: Optional[str] = None
    professorEmail: Optional[EmailStr] = None
    professorTelefone: Optional[str] = None

class ProfessorRead(ProfessorBase):
    id: int

    class Config:
        from_attributes = True