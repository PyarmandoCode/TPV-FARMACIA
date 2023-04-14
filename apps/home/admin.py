from django.contrib import admin
from .models import Categorias,Tipo_Proveedor,Proveedores,Marca,Productos,Presentacion

admin.site.register([Categorias,Tipo_Proveedor,Proveedores,Marca,Productos,Presentacion])

# admin.site.site_header = 'Proyecto Farmacia'                    # default: 