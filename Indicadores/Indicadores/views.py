from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

from django.shortcuts import render

def probandoTemplate(request):

    miHtml = open(r'C:\Users\maria\Documents\Proyecto Tercera Entrega\Producción\Indicadores\Templates\index.html')

    plantilla = Template(miHtml.read())
    
    miHtml.close()
    
    miContexto = Context()
    documento = plantilla.render(miContexto)

    return HttpResponse(documento)
 
    '''
    nom = "Mariano"
    ap = "Sirio"
    listaNotas = [1, 2, 3, 4]

    dic = {"nombre": nom, "apellido": ap, "hoy": datetime.datetime.now(), "notas": listaNotas}

    return render(request, 'index.html', dic)
'''


'''

# Create your views here.
def operarios(self):
    
    nombre = operarios(nombre="Mariano", apellido="Sirio", isla_de_produccion="Isla 1")
    operarios.save()
    documentoDeTexto = f"-->Operarios {operarios.nombre} {operarios.apellido} {operarios.isla_de_produccion}"
    
    return HttpResponse(documentoDeTexto)'''