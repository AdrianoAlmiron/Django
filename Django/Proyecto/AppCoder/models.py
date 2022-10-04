from django.db import models

# Create your models here.

class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()

class messi(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    Overall = models.IntegerField()

class cr7(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    Overall = models.IntegerField()

class neymar(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    Overall = models.IntegerField()
