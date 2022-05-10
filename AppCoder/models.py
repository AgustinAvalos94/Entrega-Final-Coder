from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Curso(models.Model):

    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Curso: {self.nombre} - Camada: {self.camada}"


class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email}"

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

# con esta indicación comenzamos a ver detalladamente en nuestra BD

    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido {self.apellido} - E-Mail {self.email} - Profesión {self.profesion}"



class Avatar(models.Model):
    #vinculo con el usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #subcarpeta avatares media
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)