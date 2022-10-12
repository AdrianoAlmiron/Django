from email.policy import default
from django.db import models
from django.utils import timezone

# Creacion de campos de la tabla 'Usuarios'
class Usuarios(models.Model):
    nombre = models.CharField(max_length=1000, default='DEFAULT VALUE')
    img= models.FileField()
    web = models.CharField(max_length=700, default='DEFAULT VALUE')
    descripcion = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_up = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'Usuarios'