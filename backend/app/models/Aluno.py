from tortoise import fields as f
from tortoise.models import Model

class Aluno(Model):
    id = f.IntField(primaty_key=True)
    alunoNome = f.CharField
    alunoEmail = f.charField
    alunoTelefone = f.charField
