from django.db import models

# Create your models here.

class Formacion(models.Model):

    titulo = models.CharField(max_length=50)
    grado = models.CharField(max_length=50)
    universidad = models.CharField(max_length=50)
    anio_recibido = models.IntegerField()


class Experiencia(models.Model):

    puesto = models.CharField(max_length=50)
    empresa = models.CharField(max_length=50)
    desde = models.IntegerField()
    hasta = models.CharField(max_length=50)
    tareas_1 = models.CharField(max_length=100)
    tareas_2 = models.CharField(max_length=100)
    tareas_3 = models.CharField(max_length=100)
    tareas_4 = models.CharField(max_length=100)
    tareas_5 = models.CharField(max_length=100)


class Skills(models.Model):

    habilidad = models.CharField(max_length=50)


class Logros(models.Model):

    detalle = models.CharField(max_length=100)
   



