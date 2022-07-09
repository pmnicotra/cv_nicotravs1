from django import forms

class Form_Formacion(forms.Form):
    titulo = forms.CharField(max_length=50)
    grado = forms.CharField(max_length=50)
    universidad = forms.CharField(max_length=50)
    anio_recibido = forms.IntegerField()
    

class Form_Experiencia(forms.Form):

    puesto = forms.CharField(max_length=50)
    empresa = forms.CharField(max_length=50)
    desde = forms.IntegerField()
    hasta = forms.CharField(max_length=50)
    tareas_1 = forms.CharField(max_length=100)
    tareas_2 = forms.CharField(max_length=100)
    tareas_3 = forms.CharField(max_length=100)
    tareas_4 = forms.CharField(max_length=100)
    tareas_5 = forms.CharField(max_length=100)


class Form_Skills(forms.Form):

    habilidad = forms.CharField(max_length=50)


class Form_Logros(forms.Form):

    detalle = forms.CharField(max_length=100)
