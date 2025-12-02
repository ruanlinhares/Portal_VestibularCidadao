from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.models import User
from app.core.security import criar_access_token

router = APIRouter()

@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await User.get_or_none(userEmail = form_data.username)
    if not user or not User.verify_password(form_data.password, user.userPassword):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais invalidas",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = criar_access_token({"sub": str(user.id)})
    return{
        "access_token": access_token,
        "token_type": "bearer",
    }
        
    