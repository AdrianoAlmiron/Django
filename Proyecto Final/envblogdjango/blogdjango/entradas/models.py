from email.policy import default
from django.db import models
from django.utils import timezone

# Creacion de campos de la tabla 'Entradas'
class Entradas(models.Model):
    titulo = models.CharField(max_length=5000, default='DEFAULT VALUE')
    contenido = models.TextField(default='DEFAULT VALUE')
    img_destacada = models.FileField()
    slug = models.CharField(max_length=5000, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    update_up = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Entradas'