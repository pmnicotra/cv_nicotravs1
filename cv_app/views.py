from django.shortcuts import render
from django.template import loader
from cv_app.models import Formacion, Experiencia, Skills, Logros
from cv_app.forms import Form_Formacion, Form_Experiencia, UserCreationForm, UserEditForm, UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

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

            return render(request, 'cv_app/vista_admin.html')

    else:
        mi_formulario = Form_Formacion()

    return render(request, 'cv_app/vista_admin.html', {'mi_formulario':mi_formulario})



def form_experiencia(request):

    if request.method == "POST":

        mi_formulario = Form_Experiencia(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data
            experiencia = Experiencia(puesto=informacion['puesto'], empresa=informacion['empresa'], desde=informacion['desde'], hasta=informacion['hasta'], tareas_1=informacion['tareas_1'], tareas_2=informacion['tareas_2'], tareas_3=informacion['tareas_3'], tareas_4=informacion['tareas_4'], tareas_5=informacion['tareas_5'])
            experiencia.save()

            return render(request, 'cv_app/vista_admin.html')

    else:
        mi_formulario = Form_Experiencia()

    return render(request, 'cv_app/experiencia_form.html', {'mi_formulario':mi_formulario})



#LOGIN

def login_request(request):
      #capturamos el post
      if request.method == "POST":
            #inicio es el uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
               
                  user = authenticate(username = usuario , password = contra)
                 
                  if user is not None:
                        login(request, user)

                        return render (request, "cv_app/vista_admin.html", {"mensaje": f"Bienvenido/a {usuario}"})
                  else:
                       
                        return render (request, "cv_app/vista_admin.html", {"mensaje":"Error en los datos"})
            else:
                  return render(request, "cv_app/vista_admin.html", {"mensaje":"Formulario erroneo"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
    
      return render(request, "cv_app/login.html", {'form': form})



def register(request):
      
      if request.method == "POST":

            form = UserCreationForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()

                  return render(request, "cv_app/vista_admin.html", {"mensaje": "usuario creado"})

      else: 
            form = UserRegisterForm()

      return render(request, "cv_app/registro.html", {"form": form})


@login_required
def editar_perfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            mi_formulario = UserEditForm(request.POST)
            if mi_formulario.is_valid(): #si pasa la validación Django
                  informacion = mi_formulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']#alg@algo.com
                  usuario.password1 = informacion['password1']#pass
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "cv_app/vista_admin.html") #vuelvo a inicio

      else:
            #creo el formulario con los datos que voy a modificar
            mi_formulario = UserEditForm(initial={'email':usuario.email})
      
      #voy al HTML que me permite editar
      return render(request, "cv_app/editar_perfil.html", {"mi_formulario": mi_formulario, "usuario": usuario})


