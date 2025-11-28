from pydantic import BaseModel
from typing import Optional

class NotaBase(BaseModel):
    alunoId: int
    alunoNota: float

class NotaCreate(NotaBase):
    pass

class NotaUpdate(BaseModel):
    alunoNota: Optional[float] = None

class NotaRead(NotaBase):
    id: int

    class Config:
        from_attributes = True