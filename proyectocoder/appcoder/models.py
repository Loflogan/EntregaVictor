from django.db import models


class Curso(models.Model):

    nombre = models.CharField(max_length=50)
    camada = models.IntegerField() 

    def __str__(self):
        return f"Curso: {self.nombre} | Camada: {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido.upper()}, {self.nombre.capitalize()}"

class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.apellido.upper()}, {self.nombre.capitalize()} [{self.profesion.title()}]"

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"{self.nombre} -> {self.fecha_de_entrega}"
