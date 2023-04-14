from .views import index,categorias_listado,categoria_form,categoria_registrar
from django.urls import path

app_name = 'home'

urlpatterns = [
    path('', index,name="index_home"),
    path('listado_categorias/', categorias_listado,name="listado_categorias"),
    path('agregar_categorias/', categoria_form,name="agregar_categoria"),
    path('registrar_categorias/', categoria_registrar,name="registrar_categoria"),
]