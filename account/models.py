from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    rut= models.CharField(max_length=9, unique=True)
    celular= models.CharField(max_length=9, unique=True)
    direccion= models.CharField(max_length=500)
    foto= models.ImageField(upload_to='media/usuario')

    def __str__(self):
        return self.username

