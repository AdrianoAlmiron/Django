from email.policy import default
from django.db import models
from django.utils import timezone

# Creacion de campos de la tabla 'categorias'
class Categorias(models.Model):
    nombre = models.CharField(max_length=100, default='DEFAULT VALUE')
    detalles = models.CharField(max_length=1000, default='DEFAULT VALUE')
    created_at = models.DateTimeField(auto_now_add=True)
    update_up = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'categorias'