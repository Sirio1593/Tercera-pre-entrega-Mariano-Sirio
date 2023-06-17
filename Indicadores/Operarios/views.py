from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render
from Operarios.models import Operarios
from Operarios.models import IslasDeProduccion
from Operarios.models import Operarios, IslasDeProduccion, CentrosDeProduccion
from django.db.models import Sum
from .models import OrdenDeProduccion, ProductosTemplate

def inicio(request):
    return render(request, "Operarios/index.html")

def operario(request):
    return render(request, "Operarios/operarios.html")

def islas(request):
    return render(request, "Operarios/islas.html")

def centros(request):
    return render(request, "Operarios/centros.html")

def productos(request):
    return render(request, "Operarios/productos.html")

def categorias(request):
    return render(request, "Operarios/categorias.html")

def ordenes(request):
    return render(request, "Operarios/ordenes.html")

def estados(request):
    return render(request, "Operarios/estados.html")

def reporte(request):
    # Retrieve the quantities produced per period and per product using aggregation
    quantities_per_period_and_product = OrdenDeProduccion.objects.values('fecha_de_inicio__year', 'fecha_de_inicio__month', 'productos_template__nombre') \
        .annotate(total_cantidad_producida=Sum('productos_template__cantidad_producida')) \
        .order_by('fecha_de_inicio__year', 'fecha_de_inicio__month')

    # Retrieve distinct product names
    products = ProductosTemplate.objects.values('nombre').distinct()

    return render(request, 'Operarios/reporte.html', {
        'quantities_per_period_and_product': quantities_per_period_and_product,
        'products': products
    })


    return render(request, 'reporte.html', {'quantities_per_period_and_product': quantities_per_period_and_product})
def sesiones(request):
    return render(request, "Operarios/sesiones.html")

def operarios(request, nom, ape, isla):
    operario = Operarios(nombre=nom, apellido=ape, isla_de_produccion=isla)
    operario.save()
    documento = f"Operario: {operario.nombre}<br>Apellido: {operario.apellido}<br>Isla: {operario.isla_de_produccion}"
    return HttpResponse(documento)
