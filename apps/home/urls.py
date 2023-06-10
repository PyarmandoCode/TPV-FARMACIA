from .views import index,Categorias_listado,Categoria_form,CreateCrudCategorias,Categoria_visualizar,DeleteCrudCategorias,UpdateCrudCategorias,Proveedores_listado,Proveedor_form,CreateCrudProveedores,DeleteCrudProveedores,Proveedor_visualizar,UpdateCrudProveedor
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', index,name="index_home"),
    path('listado_categorias/', Categorias_listado,name="listado_categorias"),
    path('agregar_categorias/', Categoria_form,name="agregar_categoria"),
    path('registrar_categorias/', CreateCrudCategorias,name="registrar_categoria"),
    path('categoria_visualizar/<int:id>', Categoria_visualizar,name="categoria_visualizar"),
    path('categoria_eliminar/', DeleteCrudCategorias.as_view(),name="categoria_eliminar"),
    path('categoria_actualizar/', UpdateCrudCategorias,name="categoria_actualizar"),
    path('listado_proveedores/', Proveedores_listado,name="listado_proveedores"),
    path('agregar_proveedores/', Proveedor_form,name="agregar_proveedores"),
    path('registrar_proveedores/', CreateCrudProveedores,name="registrar_proveedores"),
    path('proveedor_eliminar/', DeleteCrudProveedores.as_view(),name="proveedor_eliminar"),
    path('proveedor_visualizar/<int:id>', Proveedor_visualizar,name="proveedor_visualizar"),
    path('proveedor_actualizar/', UpdateCrudProveedor,name="proveedor_actualizar"),
]