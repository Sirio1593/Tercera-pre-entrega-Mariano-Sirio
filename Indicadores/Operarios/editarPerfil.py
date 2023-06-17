@login_requerid
def editarPerfil(request):
    
    usuario = request.user
    
    if request.method == "POST"
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid: #Si pasó la validación de Django
            informacion = miFormulario.cleaned_data
            #Datos que se modificarán
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()
            
            return render(request, "Operarios/index.html")
    else:
        miFomrulario= UserEditForm(initial={ 'email':usuario.email})
    return render(request, "Operarios/editarPerfil.html", {"miFormulario":miFomrulario, "usuario":usuario})
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

def PruebaLoader(self):
    nom = "Mariano"
    ap = "Sirio"
    
    dict = {"Nombre":nom, "Apellido": ap}
    plantilla = loader.get_template('index.html')
    documento = plantilla.render(dict)
    return HttpResponse(documento)
'''
# Create your views here.
def operarios(self):
    
    nombre = operarios(nombre="Mariano", apellido="Sirio", isla_de_produccion="Isla 1")
    operarios.save()
    documentoDeTexto = f"-->Operarios {operarios.nombre} {operarios.apellido} {operarios.isla_de_produccion}"
    
    return HttpResponse(documentoDeTexto)
'''

