from pydantic import BaseModel
from typing import Optional

class NotaBase(BaseModel):
    userId: int
    userNota: float

class NotaCreate(NotaBase):
    pass

class NotaUpdate(BaseModel):
    alunoNota: Optional[float] = None

class NotaRead(NotaBase):
    id: int

    class Config:
        from_attributes = True