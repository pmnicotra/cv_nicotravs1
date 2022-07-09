from django.shortcuts import render
from django.template import loader
from cv_app.models import Formacion, Experiencia
from cv_app.forms import Form_Formacion, Form_Experiencia

# Create your views here.

def inicio(request):

    return render(request, "cv_app/inicio.html")


def form_formacion(request):

    if request.method == "POST":

        mi_formulario = Form_Formacion(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data
            formacion = Formacion(titulo=informacion['titulo'], grado=informacion['grado'], universidad=informacion['universidad'], anio_recibido=informacion['anio_recibido'])
            formacion.save()

            return render(request, 'cv_app/administrador.html')

    else:
        mi_formulario = Form_Formacion()

    return render(request, 'cv_app/administrador.html', {'mi_formulario':mi_formulario})


def form_experiencia(request):

    if request.method == "POST":

        mi_formulario = Form_Experiencia(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data
            experiencia = Experiencia(puesto=informacion['puesto'], empresa=informacion['empresa'], desde=informacion['desde'], hasta=informacion['hasta'], tareas_1=informacion['tareas_1'], tareas_2=informacion['tareas_2'], tareas_3=informacion['tareas_3'], tareas_4=informacion['tareas_4'], tareas_5=informacion['tareas_5'])
            experiencia.save()

            return render(request, 'cv_app/administrador.html')

    else:
        mi_formulario = Form_Formacion()

    return render(request, 'cv_app/administrador.html', {'mi_formulario':mi_formulario})
