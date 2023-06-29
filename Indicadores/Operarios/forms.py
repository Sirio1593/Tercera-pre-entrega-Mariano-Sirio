from django import forms
from django.db import models
from .models import CategoriasDeProductos


#--------------------Sección Operarios------------------------------------
class operariosForm(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    isla_de_produccion = forms.CharField()

class buscarOperariosForm(forms.Form):
    nombre = forms.CharField()

#--------------------------------------------------------------------------


#--------------------Sección Productos------------------------------------
class productosForm(forms.Form):
    referencia_productos = forms.CharField()
    nombre = forms.CharField()
    modelo = forms.CharField()
    packaging = forms.CharField()
    categoria = forms.ModelChoiceField(queryset=CategoriasDeProductos.objects.all())
    cantidad_siendo_producida = forms.IntegerField()
    cantidad_producida = forms.IntegerField()
    cantidad_a_producir = forms.IntegerField()
    
class buscarProductosForm(forms.Form):
    nombre = forms.CharField()
#--------------------------------------------------------------------------


#--------------------Sección Categorias------------------------------------
class categoriasForm(forms.Form):
    referencia_categorias = forms.CharField()
    nombre = forms.CharField()
    
class buscarCategoriasForm(forms.Form):
    nombre = forms.CharField()
#--------------------------------------------------------------------------

#--------------------Sección Centros------------------------------------
class centrosForm(forms.Form):
    referencia_interna = forms.CharField()
    nombre = forms.CharField()
    isla_de_produccion = forms.CharField()
    capacidad = forms.CharField()
    tiempo_eficiencia = forms.CharField()
    eficiencia = forms.CharField()
    cantidad_operarios = forms.CharField()
    
class buscarCentrosForm(forms.Form):
    nombre = forms.CharField()
#--------------------------------------------------------------------------