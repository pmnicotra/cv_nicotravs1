"""cv_nicotra URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from cv_app import views
from django.contrib.auth.views import LogoutView
from cv_app.views import *
#Form_Experiencia, Form_Formacion, form_experiencia, form_formacion, form_experiencia

urlpatterns = [
   
    path('', views.sobre_mi, name="Sobre_Mi"),
    path('form_experiencia', views.form_experiencia, name="Experiencia"),
    path('form_formacion', views.form_formacion, name="Formación"),
    path('login', views.login_request, name='login'),
    path('register', views.register, name='register'),
    path('logout', LogoutView.as_view(template_name='cv_app/logout.html'), name='logout'),
    path('editar_perfil', views.editar_perfil, name='Editar_Perfil'),
    path('experiencia_cv', views.experiencia_cv, name='Experiencia_cv'),
    path('formacion_cv', views.formacion_cv, name='Formacion_cv'),
    
    path('formacion/list', views.Formacion_List.as_view(), name='List_Formacion'),
    path(r'^(?P<pk>\d+)$', views.Formacion_Detalle.as_view(), name='Detail_Formacion'),
    path(r'^nuevo$', views.Formacion_Creacion.as_view(), name='New_Formacion'),
    path(r'^editar/(?P<pk>\d+)$', views.Formacion_Update.as_view(), name='Edit_Formacion'),
    path(r'^borrar/(?P<pk>\d+)$', views.Formacion_Delete.as_view(), name='Delete_Formacion'),

]