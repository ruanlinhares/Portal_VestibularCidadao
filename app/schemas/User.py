from pydantic import BaseModel
from typing import Optional

class UserBase(BaseModel):
    userName : str
    userEmail : str
    userPhone : Optional[str] = None
    userPassword : str

class CreateUserDTO(UserBase):
    pass

class UpdateUserDTO(BaseModel):
    userName : Optional[str] = None
    userEmail : Optional[str] = None
    userPhone : Optional[str] = None
    userPassword : Optional[str] = None

class ListUserDTO(BaseModel):
    id : int
    userName : str
    userEmail : str
    userPhone : str
    