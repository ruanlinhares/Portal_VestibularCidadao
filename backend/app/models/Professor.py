from tortoise import fields as f
from tortoise.models import Model

class Professor(Model):
    id = f.IntField(primary_key=True)
    professorNome = f.CharField(max_length = 120)
    professorEmail = f.CharField(max_length = 120, unique=True)
    professorTelefone = f.CharField(max_length = 20, null=True)

    class Meta:
        table = "professores"

    def __str__(self) -> str:
        return self.professorNome