from django.contrib import admin
from .models import Categorias,Tipo_Proveedor,Proveedores,Marca,Productos,Presentacion,Color

class CategoriaAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['nom_cat', 'color_cat']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['nom_cat']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    list_filter = ['est_cat']

admin.site.register(Categorias, CategoriaAdmin)

class ProductoAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['nom_prod', 'cod_barra_prod','umedida_prod','ubicacion','pre_prod_publico']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['nom_prod']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    list_filter = ['acepta_desc_prod']

admin.site.register(Productos, ProductoAdmin)


class ProveedorAdmin(admin.ModelAdmin):
    # con esto muestras los campos que deses al mostrar la lista en admin
    list_display=['nom_prov', 'dir_prov','tel_prov','email_prov']
    # con esto añades un campo de texto que te permite realizar la busqueda, puedes añadir mas de un atributo por el cual se filtrará
    search_fields = ['nom_prov']
    # con esto añadiras una lista desplegable con la que podras filtrar (activo es un atributo booleano)
    list_filter = ['est_prov']

admin.site.register(Proveedores, ProveedorAdmin)

admin.site.register([Tipo_Proveedor,Marca,Presentacion,Color])

