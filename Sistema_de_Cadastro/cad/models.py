from django.db import models
from uuid import uuid4

# aqui crio os modelos (as tabelas)

class Usuario(models.Model):
    id_user = models.AutoField(primary_key=True, editable=False)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()