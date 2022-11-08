"""blogdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path


from categorias.views import ListadoCategorias, Primerab, Error
from detallesblog.views import DetallesBlog, CrearCategorias
from entradas.views import ListadoEntradas
from usuarios.views import ListadoUsuarios, Login

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #Categorias
    path('categorias/', ListadoCategorias.as_view(template_name="categorias/index.html"), name='ListadoCategorias'),
    path('categorias/primerab', Primerab.as_view(template_name="categorias/primerab.html"), name='Primerab'),
    path('categorias/error/', Error.as_view(template_name="categorias/error.html"), name='Error'),

    #Detalles del blog
    path('detallesblog/', DetallesBlog.as_view(template_name="detallesblog/index.html"), name='Detallesdelblog'),
    path('detallesblog/crear', CrearCategorias.as_view(template_name="detallesblog/crear.html"), name='CrearCategorias'),

    #Entradas
    path('entradas/', ListadoEntradas.as_view(template_name="entradas/index.html"), name='Entradas'),
    path('entradas/crear', CrearCategorias.as_view(template_name="entradas/crear.html"), name='CrearCategorias'),

     #Usuarios
    path('usuarios/', ListadoUsuarios.as_view(template_name="usuarios/index.html"), name='Usuarios'),
    path('usuarios/login', Login.as_view(template_name="usuarios/login.html"), name='Login'),
    
   
    
]
