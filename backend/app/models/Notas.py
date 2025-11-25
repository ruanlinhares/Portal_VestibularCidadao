from tortoise import fields as f
from tortoise.models import Model

class Notas(Model):
    id = f.IntField(primary_key=True)
    aluno = f.ForeignKeyField("models.Aluno", related_name="notas")
    alunoNota = f.IntField