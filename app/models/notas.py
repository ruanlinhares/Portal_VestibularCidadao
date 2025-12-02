from tortoise import fields as f
from tortoise.models import Model

class Notas(Model):
    id = f.IntField(primary_key=True)
    aluno = f.ForeignKeyField("models.User", related_name="notas", description = "Aluno a qual pertence a nota")
    alunoNota = f.FloatField()
    humanas = f.FloatField()
    exatas = f.FloatField()
    naturezas = f.FloatField()
    linguagens = f.FloatField()
    redacao = f.FloatField()

    class Meta:
        table = "notas"

    