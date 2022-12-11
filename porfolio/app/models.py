from django.db import models

# Create your models here.

class Proyecto(models.Model):
    foto=models.URLField()
    titulo=models.CharField(max_length=100)
    descripcion=models.CharField(max_length=200)
    tags=models.CharField(max_length=100)
    urls=models.URLField()
