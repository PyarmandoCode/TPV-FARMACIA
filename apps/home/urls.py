from .views import index,Categorias_listado,Categoria_form,CreateCrudCategorias,Categoria_visualizar,DeleteCrudCategorias,UpdateCrudCategorias,Proveedores_listado,Proveedor_form,CreateCrudProveedores,DeleteCrudProveedores,Proveedor_visualizar,UpdateCrudProveedor,TipoProvee_listado,TipoProvee_form,CreateCrudTipoProveedor,DeleteCrudTipoProveedor,UpdateCrudTipoProveedor,TipoProveedor_visualizar,Colores_listado,Colores_form,CreateCrudColor,DeleteCrudColor,TipoColor_visualizar,UpdateCrudColor,Presentacion_listado,Presentacion_form,CreateCrudPresentacion,DeleteCrudPresentacion,Presentacion_visualizar,UpdateCrudPresentacion,Marca_listado,Marca_form,CreateCrudMarca,DeleteCrudMarca,Marca_visualizar,UpdateCrudMarca,Productos_listado,Productos_form,CreateCrudProductos,DeleteCrudProductos,Productos_visualizar,UpdateCrudProductos
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
    path('listado_tipoprov/', TipoProvee_listado,name="listado_tipoprov"),
    path('agregar_tipoprov/', TipoProvee_form,name="agregar_tipoprov"),
    path('registrar_tipoprov/', CreateCrudTipoProveedor,name="registrar_tipoprov"),
    path('tipoprov_eliminar/', DeleteCrudTipoProveedor.as_view(),name="tipoprov_eliminar"),
    path('tipoprov_actualizar/', UpdateCrudTipoProveedor,name="tipoprov_actualizar"),
    path('tipoprov_visualizar/<int:id>', TipoProveedor_visualizar,name="tipoprov_visualizar"),
    path('listado_colores/', Colores_listado,name="listado_colores"),
    path('agregar_colores/', Colores_form,name="agregar_colores"),
    path('registrar_color/', CreateCrudColor,name="registrar_color"),
    path('color_eliminar/', DeleteCrudColor.as_view(),name="color_eliminar"),
    path('color_visualizar/<int:id>', TipoColor_visualizar,name="color_visualizar"),
    path('color_actualizar/', UpdateCrudColor,name="color_actualizar"),
    path('listado_presentacion/', Presentacion_listado,name="listado_presentacion"),
    path('agregar_presentacion/', Presentacion_form,name="agregar_presentacion"),
    path('registrar_presentacion/', CreateCrudPresentacion,name="registrar_presentacion"),
    path('presentacion_eliminar/', DeleteCrudPresentacion.as_view(),name="presentacion_eliminar"),
    path('presentacion_visualizar/<int:id>', Presentacion_visualizar,name="presentacion_visualizar"),
    path('presentacion_actualizar/', UpdateCrudPresentacion,name="presentacion_actualizar"),
    path('listado_marca/', Marca_listado,name="listado_marca"),
    path('agregar_marca/', Marca_form,name="agregar_marca"),
    path('registrar_marca/', CreateCrudMarca,name="registrar_marca"),
    path('marca_eliminar/', DeleteCrudMarca.as_view(),name="marca_eliminar"),
    path('marca_visualizar/<int:id>', Marca_visualizar,name="marca_visualizar"),
    path('marca_actualizar/', UpdateCrudMarca,name="marca_actualizar"),
    path('listado_productos/', Productos_listado,name="listado_productos"),
    path('agregar_productos/', Productos_form,name="agregar_productos"),
    path('registrar_productos/', CreateCrudProductos,name="registrar_productos"),
    path('productos_eliminar/', DeleteCrudProductos.as_view(),name="productos_eliminar"),
    path('productos_visualizar/<int:id>', Productos_visualizar,name="productos_visualizar"),
    path('productos_actualizar/', UpdateCrudProductos,name="productos_actualizar"),
]