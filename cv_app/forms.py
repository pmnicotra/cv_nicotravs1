from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

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


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repite la contraseña', widget=forms.PasswordInput)
    last_name = forms.CharField()
    first_name = forms.CharField()

    class Meta:
        model = User
        print(model)
        fields = ['username', 'password1', 'password2', 'last_name', 'first_name']
        help_texts= {k:"" for k in fields}

#La clase meta es una clase interna en los modelos de Django.
#Que contienen opciones Meta (metadatos) que se utilizan para
#cambiar el comportamiento de los campos de su modelo,
#como cambiar las opciones de orden, si el modelo es abstracto o no,
#versiones singulares y plurales del nombre, etc. 

class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario

    email = forms.EmailField(label='modificar email')
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

