from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    email = models.EmailField(max_length=255,unique=True)
    senha = models.CharField(max_length=24)

    def __str__(self):
        return  self.usuario
    