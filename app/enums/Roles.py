from enum import Enum

class Roles(str, Enum):
    ALUNO = "aluno"
    PROFESSOR = "professor"
    ADMIN = "admin"