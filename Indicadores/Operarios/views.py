from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render, redirect
from Operarios.forms import operariosForm
from Operarios.forms import buscarOperariosForm
from Operarios.forms import productosForm
from Operarios.forms import buscarProductosForm
from Operarios.forms import categoriasForm
from Operarios.forms import buscarCategoriasForm
from Operarios.forms import centrosForm
from Operarios.forms import buscarCentrosForm
from .models import Operarios
from .models import ProductosTemplate
from .models import CategoriasDeProductos
from .models import CentrosDeProduccion

def index(request):
    return render(request, "Operarios/index.html")

#Sección Operarios------------------------------------------------------------------------------------

def formOperarios(request):
    if request.method == 'POST':
        miForm = operariosForm(request.POST)
        print(miForm)
        if miForm.is_valid():
            inform = miForm.cleaned_data
            new_op = Operarios(nombre=inform['nombre'], apellido=inform['apellido'], isla_de_produccion=inform['isla_de_produccion'])
            try:
                new_op.save()
                print("Datos guardados correctamente")
                return render(request, "Operarios/index.html")
            except Exception as e:
                print("Error al guardar los datos:", str(e))
        else:
            print("Formulario no válido")
    else:
        miForm = operariosForm()
    return render(request, "Operarios/formOperarios.html", {"miForm":miForm})

def listaOperarios(request):
    operarios = Operarios.objects.all()  # Obtener todos los operarios de la base de datos
    return render(request, "Operarios/listaOperarios.html", {"operarios": operarios})

def buscarOperarios(request):
    if request.method == "POST":
        buscar_nombre = buscarOperariosForm(request.POST)
        
        if buscar_nombre.is_valid():
            info = buscar_nombre.cleaned_data
            operarios = Operarios.objects.filter(nombre=info["nombre"])
            return render(request, "Operarios/resultadoOperarios.html", {"operarios": operarios})
    else:
        buscar_nombre = buscarOperariosForm()
        return render(request, "Operarios/buscarOperarios.html", {"buscar_nombre": buscar_nombre})
    
def resultadoOperarios(request):
    return render(request, "Operarios/resultadoOperarios.html")

def detalle_operario(request, operario_id):
    operario = Operarios.objects.get(id=operario_id)  # Obtener el operario por su ID
    return render(request, "Operarios/detalle_operario.html", {"operario": operario})

def editar_operario(request, operario_id):
    operario = Operarios.objects.get(id=operario_id)  # Obtener el operario por su ID

    if request.method == 'POST':
        form = operariosForm(request.POST)
        if form.is_valid():
            # Procesar los datos enviados por el formulario y guardar los cambios en el operario
            operario.nombre = form.cleaned_data['nombre']
            operario.apellido = form.cleaned_data['apellido']
            operario.isla_de_produccion = form.cleaned_data['isla_de_produccion']
            operario.save()
            return redirect('detalle_operario', operario_id=operario.id)
    else:
        # Crear una instancia del formulario con los datos del operario
        form = operariosForm(initial={
            'nombre': operario.nombre,
            'apellido': operario.apellido,
            'isla_de_produccion': operario.isla_de_produccion,
        })

    return render(request, "Operarios/editar_operario.html", {"form": form})

def eliminar_operario(request, operario_id):
    operario = Operarios.objects.get(id=operario_id)  # Obtener el operario por su ID

    if request.method == 'POST':
        operario.delete()
        return redirect('listaOperarios')

    return render(request, "Operarios/eliminar_operario.html", {"operario": operario})

#------------------------------------------------------------------------------------------------------------------

#Sección Productos------------------------------------------------------------------------------------
def formProductos(request):
    if request.method == 'POST':
        miFormProduct = productosForm(request.POST)
        print(miFormProduct.errors)
        print(miFormProduct)
        if miFormProduct.is_valid():
            informP = miFormProduct.cleaned_data
            new_product = ProductosTemplate(referencia_productos=informP['referencia_productos'], nombre=informP['nombre'], modelo=informP['modelo'], packaging=informP['packaging'], categoria=informP['categoria'], cantidad_siendo_producida=informP['cantidad_siendo_producida'],cantidad_producida=informP['cantidad_producida'],cantidad_a_producir=informP['cantidad_a_producir'] )
            try:
                new_product.save()
                print("Datos guardados correctamente")
                return render(request, "Operarios/index.html")
            except Exception as e:
                print("Error al guardar los datos:", str(e))
        else:
            print("Formulario no válido")
    else:
        miFormProduct = productosForm()
    return render(request, "Operarios/formProductos.html", {"miFormProduct": miFormProduct})

def listaProductos(request):
    productos = ProductosTemplate.objects.all()  # Obtener todos los productos de la base de datos
    return render(request, "Operarios/listaProductos.html", {"productos": productos})

def buscarProductos(request):
    if request.method == "POST":
        buscar_nombre = buscarProductosForm(request.POST)
        
        if buscar_nombre.is_valid():
            info = buscar_nombre.cleaned_data
            productos = ProductosTemplate.objects.filter(nombre=info["nombre"])
            return render(request, "Operarios/resultadoProductos.html", {"productos": productos})
    else:
        buscar_nombre = buscarProductosForm()
        return render(request, "Operarios/buscarProductos.html", {"buscar_nombre": buscar_nombre})
    
def resultadoProducto(request):
    return render(request, "Operarios/resultadoOperarios.html")

def detalle_producto(request, producto_id):
    producto = ProductosTemplate.objects.get(id=producto_id)  # Obtener el producto por su ID
    return render(request, "Operarios/detalle_producto.html", {"producto": producto})

def editar_producto(request, producto_id):
    producto = ProductosTemplate.objects.get(id=producto_id)  # Obtener el operario por su ID

    if request.method == 'POST':
        form = productosForm(request.POST)
        if form.is_valid():
            # Procesar los datos enviados por el formulario y guardar los cambios en el producto
            producto.referencia_productos = form.cleaned_data['referencia_productos']
            producto.nombre = form.cleaned_data['nombre']
            producto.modelo = form.cleaned_data['modelo']
            producto.packaging = form.cleaned_data['packaging']
            producto.categoria = form.cleaned_data['categoria']
            producto.save()
            return redirect('detalle_producto', producto_id=producto.id)
        
    else:
        # Crear una instancia del formulario con los datos del producto
        form = productosForm(initial={
            'referencia_productos': producto.referencia_productos,
            'nombre': producto.nombre,
            'modelo': producto.modelo,
            'packaging': producto.packaging,
            'categorias': producto.categoria,
        })

    return render(request, "Operarios/editar_producto.html", {"form": form})

def eliminar_producto(request, producto_id):
    producto = ProductosTemplate.objects.get(id=producto_id)  # Obtener el operario por su ID

    if request.method == 'POST':
        producto.delete()
        return redirect('listaProductos')

    return render(request, "Operarios/eliminar_producto.html", {"producto": producto})

#------------------------------------------------------------------------------------------------------------------


#Sección Productos------------------------------------------------------------------------------------
def formCategorias(request):
    if request.method == 'POST':
        miFormCateg = categoriasForm(request.POST)
        print(miFormCateg.errors)
        print(miFormCateg)
        if miFormCateg.is_valid():
            informC = miFormCateg.cleaned_data
            new_categ = CategoriasDeProductos(referencia_categorias=informC['referencia_categorias'], nombre=informC['nombre'] )
            try:
                new_categ.save()
                print("Datos guardados correctamente")
                return render(request, "Operarios/index.html")
            except Exception as e:
                print("Error al guardar los datos:", str(e))
        else:
            print("Formulario no válido")
    else:
        miFormCateg = categoriasForm()
    return render(request, "Operarios/formCategorias.html", {"miFormCateg": miFormCateg})


def listaCategorias(request):
    categorias = CategoriasDeProductos.objects.all()  # Obtener todos los productos de la base de datos
    return render(request, "Operarios/listaCategorias.html", {"categorias": categorias})

def buscarCategorias(request):
    if request.method == "POST":
        buscar_nombre = buscarCategoriasForm(request.POST)
        
        if buscar_nombre.is_valid():
            info = buscar_nombre.cleaned_data
            categorias = CategoriasDeProductos.objects.filter(nombre=info["nombre"])
            return render(request, "Operarios/resultadoCategorias.html", {"categorias": categorias})
    else:
        buscar_nombre = buscarCategoriasForm()
        return render(request, "Operarios/buscarCategorias.html", {"buscar_nombre": buscar_nombre})
    
def resultadoCategorias(request):
    return render(request, "Operarios/resultadoCategorias.html")

def detalle_categoria(request, categoria_id):
    categoria = CategoriasDeProductos.objects.get(id=categoria_id)
    return render(request, "Operarios/detalle_categoria.html", {"categoria": categoria})

def editar_categoria(request, categoria_id):
    categoria = CategoriasDeProductos.objects.get(id=categoria_id)

    if request.method == 'POST':
        formCateg = categoriasForm(request.POST)
        if formCateg.is_valid():

            categoria.referencia_categorias = formCateg.cleaned_data['referencia_categorias']
            categoria.nombre = formCateg.cleaned_data['nombre']
            categoria.save()
            return render(request, 'Operarios/detalle_categoria.html', {'categoria': categoria_id})

        
    else:
        # Crear una instancia del formulario con los datos del producto
        formCateg = categoriasForm(initial={
            'referencia_categorias': categoria.referencia_categorias,
            'nombre': categoria.nombre,
        })

    return render(request, "Operarios/editar_categoria.html", {"formCateg": formCateg})

def eliminar_categoria(request, categoria_id):
    categoria = CategoriasDeProductos.objects.get(id=categoria_id)  # Obtener el operario por su ID

    if request.method == 'POST':
        categoria.delete()
        return redirect('listaCategorias')

    return render(request, "Operarios/eliminar_categoria.html", {"categoria": categoria})

#------------------------------------------------------------------------------------------------------------------