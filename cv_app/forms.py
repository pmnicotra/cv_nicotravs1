from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Form_Formacion(forms.Form):
    titulo = forms.CharField(max_length=50)
    grado = forms.CharField(max_length=50)
    universidad = forms.CharField(max_length=50)
    año_recibido = forms.IntegerField()
    

class Form_Experiencia(forms.Form):

    puesto = forms.CharField(max_length=50)
    empresa = forms.CharField(max_length=50)
    desde = forms.CharField(max_length=50)
    hasta = forms.CharField(max_length=50)
    tareas = forms.CharField(max_length=100)


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


class UserEditForm(UserCreationForm): 
    
    email = forms.EmailField(label='Modificar email')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts= {k:"" for k in fields}

