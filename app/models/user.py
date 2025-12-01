from tortoise import fields as f
from tortoise.models import Model
from app.enums import Roles

class User(Model):
    id = f.IntField(primary_key=True)
    userName = f.CharField(max_length = 120)
    userEmail = f.CharField(max_length = 150, unique=True)
    userPhone = f.CharField(max_length = 20, null=True)
    userPassword = f.CharField(max_length = 120)
    userRole = f.CharEnumField(Roles, default= Roles.ALUNO)

    class Meta():
        table = "Users"

    def __str__(self):
        return f"User(id = {self.userName}, id = {self.id}, name = {self.userName}, email = {self.userEmail}, phone = {self.userPhone}, role = {self.userPhone} )"