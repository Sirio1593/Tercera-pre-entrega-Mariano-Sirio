from django.db import models
from django.core.validators import MaxValueValidator

class Operarios(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    isla_de_produccion = models.CharField(max_length=40)

class IslasDeProduccion(models.Model):
    nombre = models.CharField(max_length=40)  # Nombre del centro de producción
    ubicacion = models.CharField(max_length=40)
    cantidad_operarios = models.IntegerField()

class CentrosDeProduccion(models.Model):
    referencia_interna = models.CharField(max_length=40) 
    nombre = models.CharField(max_length=40)  # Nombre del centro de producción
    isla_de_produccion = models.CharField(max_length=40)  # Ubicación del centro de producción
    capacidad = models.IntegerField(validators=[MaxValueValidator(9999)])  # Capacidad máxima del centro de producción
    tiempo_eficiencia = models.IntegerField()  # Tiempo de eficiencia del centro de producción en minutos
    eficiencia = models.IntegerField()  # Eficiencia del centro de producción (porcentaje)
    cantidad_operarios = models.IntegerField()  # Cantidad de operarios en el centro de producción

class CategoriasDeProductos(models.Model):
    referencia_categorias = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)

class ProductosTemplate(models.Model):
    referencia_productos = models.CharField(max_length=40)
    nombre = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
    packaging = models.CharField(max_length=40)
    #imagen = models.ImageField(upload_to='productos/')
    categoria = models.ForeignKey(CategoriasDeProductos, on_delete=models.CASCADE)
    cantidad_siendo_producida = models.IntegerField()
    cantidad_producida = models.IntegerField()
    cantidad_a_producir = models.IntegerField()

class EstadosDeOrden(models.Model):
    nombre = models.CharField(max_length=40)
    
class OrdenDeProduccion(models.Model):
    estado = models.ForeignKey(EstadosDeOrden, on_delete=models.CASCADE)
    referencia_orden = models.CharField(max_length=40)
    centro_de_produccion = models.ForeignKey(CentrosDeProduccion, on_delete=models.CASCADE)
    productos_template = models.ForeignKey(ProductosTemplate, on_delete=models.CASCADE)
    cantidad_a_producir = models.IntegerField()
    fecha_de_inicio = models.DateTimeField()
    fecha_de_finalizacion = models.DateTimeField()
    duracion = models.DurationField()