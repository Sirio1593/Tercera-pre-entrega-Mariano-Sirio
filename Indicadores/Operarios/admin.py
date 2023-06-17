from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Operarios)
admin.site.register(IslasDeProduccion)
admin.site.register(CentrosDeProduccion)
admin.site.register(CategoriasDeProductos)
admin.site.register(ProductosTemplate)
admin.site.register(EstadosDeOrden)
admin.site.register(OrdenDeProduccion)
