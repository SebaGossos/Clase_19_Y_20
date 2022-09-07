from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(unique=True)
    #activo = models.BooleanField(default=True)

    def __str__(self):
        return f'Curso nombre: {self.nombre}, camada: {self.camada}'
    

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=33)
    apellido = models.CharField(max_length=33)
    email = models.EmailField(unique=True)

class Profesor(models.Model):
    nombre = models.CharField(max_length=33)
    apellido = models.CharField(max_length=33)
    email = models.EmailField(unique=True)
    profesion = models.CharField(max_length=33)

class Entregable(models.Model):
    nombre = models.CharField(max_length=33)
    FechaDeEntrega = models.DateField()
    Entregado = models.BooleanField()
