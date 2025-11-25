from tortoise import fields as f
from tortoise.models import Model

class Aluno(Model):
    id = f.IntField(primary_key=True)
    alunoNome = f.CharField
    alunoEmail = f.CharField
    alunoTelefone = f.CharField
