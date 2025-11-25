from tortoise import fields as f
from tortoise.models import Model

class Notas(Model):
    id = f.IntField(primary_key=True)
    professorNome = f.CharField
    professorEmail = f.CharField
    professorTelefone = f.CharField