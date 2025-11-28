from tortoise import fields as f
from tortoise.models import Model
from app.enums.roles import Roles

class User(Model):
    id = f.IntField(primary_key=True)
    userName = f.CharField(max_length = 120)
    userEmail = f.CharField(max_length = 150, unique=True)
    userPhone = f.CharField(ax_length = 20, null=True)
    userPassword = f.CharField(max_length = 120)
    userRole = f.CharEnumField(Roles, default= Roles.ALUNO)

    class Meta():
        table = "Users"

    class __str__(self):
        return