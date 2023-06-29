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
from django.urls import path
from Operarios.views import *


urlpatterns = [
    
    path('', index, name='Index'),
    path('Index', index, name='Index'),

    path('buscarOperarios', buscarOperarios, name='buscarOperarios'),
    path('formOperarios', formOperarios, name="formOperarios"),
    path('resultadoOperarios', resultadoOperarios, name="resultadoOperarios"),
    path('listaOperarios', listaOperarios, name="listaOperarios"),
    path('operario/<int:operario_id>/', detalle_operario, name='detalle_operario'),
    path('operario/<int:operario_id>/editar/', editar_operario, name='editar_operario'),
    path('operario/<int:operario_id>/eliminar/', eliminar_operario, name='eliminar_operario'),

    path('formProductos', formProductos, name='formProductos'),
    path('buscarProductos', buscarProductos, name='buscarProductos'),
    path('resultadoProducto', resultadoProducto, name="resultadoProducto"),
    path('listaProductos', listaProductos, name="listaProductos"),
    path('producto/<int:producto_id>/', detalle_producto, name='detalle_producto'),
    path('producto/<int:producto_id>/editar/', editar_producto, name='editar_producto'),
    path('producto/<int:producto_id>/eliminar/', eliminar_producto, name='eliminar_producto'),
    

    path('formCategorias', formCategorias, name='formCategorias'),
    path('buscarCategorias', buscarCategorias, name='buscarCategorias'),
    path('resultadoCategorias', resultadoCategorias, name="resultadoCategorias"),
    path('listaCategorias', listaCategorias, name="listaCategorias"),
    path('categoria/<int:categoria_id>/', detalle_categoria, name='detalle_categoria'),
    path('categoria/<int:categoria_id>/editar/', editar_categoria, name='editar_categoria'),
    path('categoria/<int:categoria_id>/eliminar/', eliminar_categoria, name='eliminar_categoria'),
    path('categoria/<int:categoria_id>/editar/', editar_categoria, name='editar_categoria'),
    
]