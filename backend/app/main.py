from fastapi import FastAPI
from app.api.api import api_router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.include_router(api_router)

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["app.models.Aluno", "app.models.Notas", "app.models.Professor"]},
    generate_schemas=True,
    add_exception_handlers=True,
)