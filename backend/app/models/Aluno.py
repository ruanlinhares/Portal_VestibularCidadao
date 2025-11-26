from enum import unique
from tortoise import fields as f
from tortoise.models import Model

class Aluno(Model):
    id = f.IntField(primary_key=True)
    alunoNome = f.CharField(max_length = 120)
    alunoEmail = f.CharField(max_length = 150, unique=True)
    alunoTelefone = f.CharField(max_length = 20, null=True)

    class Meta:
        table = "alunos"

    def __str__(self) -> str:
        return self.alunoNome