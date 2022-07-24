from django.db import models

# Create your models here.

class Formacion(models.Model):

    titulo = models.CharField(max_length=50)
    grado = models.CharField(max_length=50)
    universidad = models.CharField(max_length=50)
    año_recibido = models.IntegerField()

    def __str__(self):return f"Título: {self.titulo} - Grado: {self.grado} - Universidad: {self.universidad} - Año_Recibido: {self.año_recibido}"



class Experiencia(models.Model):

    puesto = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    desde = models.CharField(max_length=50)
    hasta = models.CharField(max_length=50)
    tareas = models.CharField(max_length=100)

    def __str__(self):return f"Puesto: {self.puesto} - Empresa: {self.empresa} - Desde: {self.desde} - Hasta: {self.hasta}, Tareas: {self.tareas}"
   



