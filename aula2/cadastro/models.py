from django.db import models

# Create your models here.
class Cadastro(models.Model):
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pais = models.CharField(max_length=50)
