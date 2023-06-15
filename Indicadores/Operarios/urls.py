from django.urls import path
from Operarios import views

urlpatterns = [
    path('', views.vista_inicio),
    path('Operarios', views.vista_Operarios, name="Operarios de Producción"),
    path('Islas', views.vista_Islas, name="Islas de Producción"),
    path('Centros', views.vista_Centros, name="Centros de Producción"),
    path('Productos', views.vista_Productos, name="Productos"),
]
