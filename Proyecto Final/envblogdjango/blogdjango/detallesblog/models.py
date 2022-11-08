from email.policy import default
from django.db import models
from django.utils import timezone

# Creacion de campos de la tabla 'Detallesblog'
class DetallesBlog(models.Model):
    detalles = models.CharField(max_length=60000, default='DEFAULT VALUE')
    logo = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_up = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'DetallesBlog'