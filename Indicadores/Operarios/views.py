from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

def vista_inicio(request):
    
    return HttpResponse('Inicio')

def vista_Operarios(request):
    
    return HttpResponse('Operarios')

def vista_Islas(request):
    
    return HttpResponse('Islas de Producción')

def vista_Centros(request):

    return HttpResponse('Centros de Producción')

def vista_Productos(request):
    
    return HttpResponse('Productos')