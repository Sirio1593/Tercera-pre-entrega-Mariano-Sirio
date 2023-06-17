"""
URL configuration for Indicadores project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from .views import inicio
from .views import islas
from .views import operario
from .views import centros
from .views import productos
from .views import categorias
from .views import ordenes
from .views import estados
from .views import reporte
from .views import sesiones


urlpatterns = [
    path('', inicio, name='inicio'),
    path('Operarios', operario, name='operario'),
    path('Islas', islas, name='isla'),
    path('Centros de Producción', centros, name='centro'),
    path('Productos', productos, name='producto'),
    path('Categorias', categorias, name='categoria'),
    path('Ordenes', ordenes, name='orden'),
    path('Estados', estados, name='estado'),
    path('Reporte', reporte, name='reporte'),
    path('Sesion', sesiones, name='sesion'),
    
]
