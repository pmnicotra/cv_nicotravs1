from ast import For
from django.shortcuts import render
from django.template import loader
from cv_app.models import Formacion, Experiencia
from cv_app.forms import Form_Formacion, Form_Experiencia, UserCreationForm, UserEditForm, UserRegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

def inicio(request):

    return render(request, "cv_app/inicio.html")

@login_required
def form_formacion(request):

    if request.method == "POST":

        mi_formulario = Form_Formacion(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data
            formacion = Formacion(titulo=informacion['titulo'], grado=informacion['grado'], universidad=informacion['universidad'], año_recibido=informacion['año_recibido'])
            formacion.save()

            return render(request, 'cv_app/vista_admin.html')

    else:
        mi_formulario = Form_Formacion()

    return render(request, 'cv_app/formacion1_form.html', {'mi_formulario':mi_formulario})


@login_required
def form_experiencia(request):

    if request.method == "POST":

        mi_formulario = Form_Experiencia(request.POST)
        print(mi_formulario)

        if mi_formulario.is_valid:

            informacion = mi_formulario.cleaned_data
            experiencia = Experiencia(puesto=informacion['puesto'], empresa=informacion['empresa'], desde=informacion['desde'], hasta=informacion['hasta'], tareas=informacion['tareas'])
            experiencia.save()

            return render(request, 'cv_app/vista_admin.html')

    else:
        mi_formulario = Form_Experiencia()

    return render(request, 'cv_app/experiencia_form.html', {'mi_formulario':mi_formulario})


#CRUD FORMACION

class Formacion_List(ListView):
      model = Formacion
      template_name = 'cv_app/form_list.html'

class Formacion_Detalle(DetailView):
      model = Formacion
      template_name = 'cv_app/form_detalle.html'

class Formacion_Creacion(CreateView):
      model = Formacion
      success_url = '/cv_app/formacion/list'
      fields = ['titulo', 'grado', 'universidad', 'año_recibido']

class Formacion_Update(UpdateView):
      model = Formacion
      success_url = '/cv_app/formacion/list'
      fields = ['titulo', 'grado', 'universidad', 'año_recibido']

class Formacion_Delete(DeleteView):
      model = Formacion
      success_url = '/cv_app/formacion/list'



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

      usuario = request.user
      
      if request.method == 'POST':
            mi_formulario = UserEditForm(request.POST)
            if mi_formulario.is_valid(): 
                  informacion = mi_formulario.cleaned_data
                  
                  usuario.email = informacion['email']
                  usuario.password1 = informacion['password1']
                  usuario.password2 = informacion['password2']
                  usuario.save()
            
                  return render(request, "cv_app/vista_admin.html")

      else:
            mi_formulario = UserEditForm(initial={'email':usuario.email})
      
      return render(request, "cv_app/editar_perfil.html", {"mi_formulario": mi_formulario, "usuario": usuario})


def experiencia_cv(request):

      experiencia = Experiencia.objects.all()
      print(experiencia)
      return render(request, "cv_app/experiencia_cv.html", {'exp':experiencia})

def formacion_cv(request):

      formacion = Formacion.objects.all()
      return render(request, "cv_app/formacion_cv.html", {'form':formacion})      

def sobre_mi(request):

      return render(request, "cv_app/sobre_mi.html")


