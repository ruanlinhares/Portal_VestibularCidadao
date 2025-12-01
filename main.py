from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.api.api import api_router
from app.core.config import Settings

app = FastAPI(tittle="Portal Vestibular Cidadão")
app.include_router(api_router, prefix="/api")

register_tortoise(
    app,
    db_url="mysql://root:root@localhost:3306/baseVC",
    modules={"models": ["app.models.user", "app.models.notas"]},
    generate_schemas=True,
    add_exception_handlers=True,
)