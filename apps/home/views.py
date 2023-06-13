from django.shortcuts import render
from .models import Categorias,Color,Proveedores,Tipo_Proveedor,Presentacion,Marca,Productos
from django.http import JsonResponse
from django.views.generic import  View

def index(request):
    template_name = "Index.html"
    return render(request, template_name)

#region Categorias
def Categorias_listado(request):
    categorias = Categorias.objects.filter(est_cat=True)
    context = {
        "Categorias": categorias,
    }
    template_name = "Listado_categorias.html"
    return render(request, template_name, context)

def Categoria_visualizar(request,id):
    template_name = "Visualizar_categoria.html"
    categoria=Categorias.objects.get(id=id)
    color=Color.objects.filter(est_color=True)

    #Seleccionado la categoria para mostrarla en el Combo
    colors=Color.objects.get(id=categoria.color_cat.id)
    context = {"categorias":
               categoria,"Colores":color,"colorseleccionado":colors.nom_color}
    return render(request, template_name,context)


class DeleteCrudCategorias(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Categorias.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    
    
def Categoria_form(request):
    color=Color.objects.filter(est_color=True)
    context = {
        "Colores":color
    }
    template_name = "Nueva_categoria.html"
    return render(request, template_name,context)

def CreateCrudCategorias(request):
    response_data = {}
    template_name="Nueva_categoria.html"
    if request.POST.get('action') =='registrar_categoria':
        try:
            nombre_categoria = request.POST.get('txtnomcat')
            descripcion_categoria = request.POST.get('txtdescripcion')
            color_categoria = request.POST.get('cmbcolor')
            color=Color.objects.get(id=color_categoria)
            file = request.FILES.get('imgcat')
            Categorias.objects.create(nom_cat=nombre_categoria,des_cat=descripcion_categoria,color_cat=color,img_cat=file)
            
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No se Registro la Categoria Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Registro con exito la Categoria'   
        return JsonResponse(response_data)   
    return render(request,template_name) 


def UpdateCrudCategorias(request):
    response_data = {}
    template_name="Visualizar_categoria.html"
    if request.POST.get('action') =='actualizar_categoria':
        try:
            id=request.POST.get('id')
            categoria = Categorias.objects.get(id=id)
            categoria.nom_cat=request.POST.get('txtnomcat')
            categoria.des_cat=request.POST.get('txtdescripcion')
            color_categoria = request.POST.get('cmbcolor')
            if color_categoria=="":
                color=categoria.color_cat
            else:
                color=Color.objects.get(id=color_categoria)
            categoria.color_cat=color
            file = request.FILES.get('imgcat')
            if file:
                categoria.img_cat=file
            categoria.save()
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No Se Modifico la Categoria Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Modifico con exito la Categoria'  
            
             
        return JsonResponse(response_data)   
    return render(request,template_name) 

#endregion Description

#region Proveedores            
def Proveedores_listado(request):
    proveedores = Proveedores.objects.filter(est_prov=True)
    context = {
        "Proveedores": proveedores,
    }
    template_name = "Listado_proveedores.html"
    return render(request, template_name, context)


def Proveedor_form(request):
    tipo=Tipo_Proveedor.objects.filter(est_tip_prov=True)
    context = {
        "Tipo":tipo
    }
    template_name = "Nuevo_proveedor.html"
    return render(request, template_name,context)


def CreateCrudProveedores(request):
    response_data = {}
    template_name="Nuevo_proveedor.html"
    if request.POST.get('action') =='registrar_proveedor':
        try:
            nombre_proveedor = request.POST.get('txtnomprov')
            descripcion_proveedor = request.POST.get('txtdescripcion')
            dir_proveedor = request.POST.get('txtdirprov')
            doc_proveedor = request.POST.get('txtdocprov')
            tlf_proveedor = request.POST.get('txttelprov')
            email_proveedor = request.POST.get('txtemailprov')
            contacto_proveedor = request.POST.get('txtcontactoprov')
            tipo_proveedor = request.POST.get('cmbtproveedor')
            tipo=Tipo_Proveedor.objects.get(id=tipo_proveedor)
            
            Proveedores.objects.create(nom_prov=nombre_proveedor,des_prov=descripcion_proveedor,dir_prov=dir_proveedor,doc_prov=doc_proveedor,tel_prov=tlf_proveedor,email_prov=email_proveedor,contacto_prov=contacto_proveedor,tipo_prov=tipo)
            
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No se Registro El Proveedor Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Registro con exito El Proveedor'   
        return JsonResponse(response_data)   
    return render(request,template_name) 

class DeleteCrudProveedores(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Proveedores.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

def Proveedor_visualizar(request,id):
    template_name = "Visualizar_proveedor.html"
    proveedor=Proveedores.objects.get(id=id)
    tipo=Tipo_Proveedor.objects.filter(est_tip_prov=True)

    #Seleccionado el tipo para mostrarla en el Combo
    tipos=Tipo_Proveedor.objects.get(id=proveedor.tipo_prov.id)
    
    context = {"proveedor":proveedor,
               "tipo":tipo,"tiposeleccionado":tipos.tip_prov}
    return render(request, template_name,context)   


def UpdateCrudProveedor(request):
    response_data = {}
    template_name="Visualizar_proveedor.html"
    if request.POST.get('action') =='actualizar_proveedor':
        try:
            id=request.POST.get('id')
            proveedor = Proveedores.objects.get(id=id)
            proveedor.nom_prov=request.POST.get('txtnom')
            proveedor.des_prov=request.POST.get('txtdescripcion')
            proveedor.dir_prov=request.POST.get('txtdir')
            proveedor.doc_prov=request.POST.get('txtdoc')
            proveedor.tlf_prov=request.POST.get('txtfono')
            proveedor.email_prov=request.POST.get('txtemail')
            proveedor.contacto_prov=request.POST.get('txtcontacto')
            tipo_proveedor = request.POST.get('cmbtipo')
            if tipo_proveedor=="":
                tipo=proveedor.tipo_prov
            else:
                tipo=Tipo_Proveedor.objects.get(id=tipo_proveedor)
                
            proveedor.tipo_prov=tipo
            proveedor.save()
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No Se Modifico el Proveedor Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Modifico con exito El Proveedor'  
            
             
        return JsonResponse(response_data)   
    return render(request,template_name) 

#endregion Proveedores

#region TProveedores 

def TipoProvee_listado(request):
    Tprov = Tipo_Proveedor.objects.filter(est_tip_prov=True)
    context = {
        "tipoprov": Tprov,
    }
    template_name = "Listado_tipo_proveedor.html"
    return render(request, template_name, context)

def TipoProvee_form(request):
    template_name = "Nuevo_tipo_proveedor.html"
    return render(request, template_name)

def CreateCrudTipoProveedor(request):
    response_data = {}
    template_name="Nuevo_tipo_proveedor.html"
    if request.POST.get('action') =='registrar_tproveedor':
        try:
            nombre_tproveedor = request.POST.get('txtnomtprov')
            descripcion_tproveedor = request.POST.get('txtdescripcion')
            
            Tipo_Proveedor.objects.create(tip_prov=nombre_tproveedor,des_tip_prov=descripcion_tproveedor)
            
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No se Registro El Tipo de Proveedor Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Registro con exito El Tipo  Proveedor'   
        return JsonResponse(response_data)   
    return render(request,template_name) 

class DeleteCrudTipoProveedor(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Tipo_Proveedor.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    
def TipoProveedor_visualizar(request,id):
    template_name = "Visualizar_tipo_proveedor.html"
    tproveedor=Tipo_Proveedor.objects.get(id=id)
    
    context = {"tipoprov":tproveedor,
               }
    return render(request, template_name,context)     
    
def UpdateCrudTipoProveedor(request):
    response_data = {}
    template_name="Visualizar_tipo_proveedor.html"
    if request.POST.get('action') =='actualizar_tproveedor':
        try:
            id=request.POST.get('id')
            tproveedor = Tipo_Proveedor.objects.get(id=id)
            tproveedor.tip_prov=request.POST.get('txtnomtprov')
            tproveedor.des_tip_prov=request.POST.get('txtdescripcion')
            tproveedor.save()
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No Se Modifico el Tipo de Proveedor Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Modifico con exito el Tipo de Proveedor'  
            
             
        return JsonResponse(response_data)   
    return render(request,template_name) 

#endregion TProveedores

#region Colores
def Colores_listado(request):
    color = Color.objects.filter(est_color=True)
    context = {
        "colores": color,
    }
    template_name = "Listado_colores.html"
    return render(request, template_name, context)

def Colores_form(request):
    template_name = "Nuevo_colores.html"
    return render(request, template_name)

def CreateCrudColor(request):
    response_data = {}
    template_name="Nuevo_colores.html"
    if request.POST.get('action') =='registrar_colores':
        try:
            nombre_color = request.POST.get('txtnomcol')
            Color.objects.create(nom_color=nombre_color)
            
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No se Registro El Color Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Registro con exito El Color'   
        return JsonResponse(response_data)   
    return render(request,template_name) 

class DeleteCrudColor(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Color.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    
def TipoColor_visualizar(request,id):
    template_name = "Visualizar_color.html"
    color=Color.objects.get(id=id)
    context = {"color":color,
               }
    return render(request, template_name,context)     

def UpdateCrudColor(request):
    response_data = {}
    template_name="Visualizar_color.html"
    if request.POST.get('action') =='actualizar_color':
        try:
            id=request.POST.get('id')
            color = Color.objects.get(id=id)
            color.nom_color=request.POST.get('txtnomcol')
            color.save()
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No Se Modifico el Color Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Modifico con exito el Color'  
            
        return JsonResponse(response_data)   
    return render(request,template_name) 

#endregion colores

#region presentacion
def Presentacion_listado(request):
    presentacion = Presentacion.objects.filter(est_pre=True)
    context = {
        "presentacion": presentacion,
    }
    template_name = "Listado_presentacion.html"
    return render(request, template_name, context)


def Presentacion_form(request):
    template_name = "Nuevo_presentacion.html"
    return render(request, template_name)


def CreateCrudPresentacion(request):
    response_data = {}
    template_name="Nuevo_presentacion.html"
    if request.POST.get('action') =='registrar_presentacion':
        try:
            nombre_presentacion = request.POST.get('txtnompre')
            descripcion_presentacion = request.POST.get('txtdescripcion')
            
            Presentacion.objects.create(nom_pre=nombre_presentacion,des_pre=descripcion_presentacion)
            
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No se Registro la Presentacion Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Registro con exito la presentacion'   
        return JsonResponse(response_data)   
    return render(request,template_name) 


class DeleteCrudPresentacion(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Presentacion.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    
def Presentacion_visualizar(request,id):
    template_name = "Visualizar_presentacion.html"
    presentacion=Presentacion.objects.get(id=id)
    context = {"presentacion":presentacion,
               }
    return render(request, template_name,context)     

def UpdateCrudPresentacion(request):
    response_data = {}
    template_name="Visualizar_presentacion.html"
    if request.POST.get('action') =='actualizar_presentacion':
        try:
            id=request.POST.get('id')
            presentacion = Presentacion.objects.get(id=id)
            presentacion.nom_pre=request.POST.get('txtnompre')
            presentacion.des_pre=request.POST.get('txtdescripcion')
            presentacion.save()
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No Se Modifico la Presentacion Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Modifico con exito la presentacion'  
        return JsonResponse(response_data)   
    return render(request,template_name) 

#endregion presentacion

#region marca
def Marca_listado(request):
    marca = Marca.objects.filter(est_marca=True)
    context = {
        "marca": marca,
    }
    template_name = "Listado_marca.html"
    return render(request, template_name, context)

def Marca_form(request):
    template_name = "Nuevo_marca.html"
    return render(request, template_name)

def CreateCrudMarca(request):
    response_data = {}
    template_name="Nueva_marca.html"
    if request.POST.get('action') =='registrar_marca':
        try:
            nombre_marca = request.POST.get('txtnom_marca')
            descripcion_marca = request.POST.get('txtdescripcion')
            file = request.FILES.get('imgmarca')
            Marca.objects.create(nom_marca=nombre_marca,des_marca=descripcion_marca,img_marca=file)
            
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No se Registro la Marca Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Registro con exito la Marca'   
        return JsonResponse(response_data)   
    return render(request,template_name) 

class DeleteCrudMarca(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Marca.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    
def Marca_visualizar(request,id):
    template_name = "Visualizar_marca.html"
    marca=Marca.objects.get(id=id)
    context = {"marca":marca,
               }
    return render(request, template_name,context)     


def UpdateCrudMarca(request):
    response_data = {}
    template_name="Visualizar_marca.html"
    if request.POST.get('action') =='actualizar_marca':
        try:
            id=request.POST.get('id')
            marca = Marca.objects.get(id=id)
            marca.nom_marca=request.POST.get('txtnom_mar')
            marca.des_marca=request.POST.get('txtdescripcion')
            file = request.FILES.get('imgmarca')
            if file:
                marca.img_marca=file
            marca.save()
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No Se Modifico la Marca Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Modifico con exito la Marca'  
            
             
        return JsonResponse(response_data)   
    return render(request,template_name) 
#endregion marca

def Productos_listado(request):
    productos = Productos.objects.filter(est_prod=True)
    context = {
        "productos": productos,
    }
    template_name = "Listado_productos.html"
    return render(request, template_name, context)

def Productos_form(request):
    template_name = "Nuevo_productos.html"
    color=Color.objects.filter(est_color=True)
    categoria=Categorias.objects.filter(est_cat=True)
    proveedor=Proveedores.objects.filter(est_prov=True)
    marca=Marca.objects.filter(est_marca=True)
    presentacion=Presentacion.objects.filter(est_pre=True)

    context = {
        "Colores":color,"Categorias":categoria,"Proveedores":proveedor,"Marcas":marca,"Presentacion":presentacion
    }
    return render(request, template_name,context)

def CreateCrudProductos(request):
    response_data = {}
    template_name="Nuevo_productos.html"
    if request.POST.get('action') =='registrar_productos':
        try:
            nombre_producto = request.POST.get('txtnomprod')
            barra_producto = request.POST.get('txtcodbarra')
            etiqueta_producto = request.POST.get('txtetiqueta')
            des_producto = request.POST.get('txtdescripcion')
            umedida_producto = request.POST.get('txtumedida')
            ubicacion_producto = request.POST.get('txtubicacion')
            color_producto = request.POST.get('cmbcolor')
            color=Color.objects.get(id=color_producto)
            categoria_producto = request.POST.get('cmbcategoria')
            categoria=Categorias.objects.get(id=categoria_producto)
            proveedor_producto = request.POST.get('cmbproveedor')
            proveedor=Proveedores.objects.get(id=proveedor_producto)
            marca_producto = request.POST.get('cmbmarca')
            marca=Marca.objects.get(id=marca_producto)
            presentacion_producto = request.POST.get('cmbpresentacion')
            presentacion=Presentacion.objects.get(id=presentacion_producto)
            file = request.FILES.get('imgprod')
            Productos.objects.create(nom_prod=nombre_producto,
                                      cod_barra_prod=barra_producto,
                                      nom_etiqueta_prod=etiqueta_producto,
                                      des_prod=des_producto,
                                      umedida_prod=umedida_producto,
                                      ubicacion=ubicacion_producto,
                                      color_prod=color,
                                      img_prod=file,
                                      cat_prod=categoria,
                                      prov_prod=proveedor,
                                      marca_prod= marca,
                                      present_prod=presentacion
                                      )
            
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No se Registro el Producto Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Registro con exito el Producto'   
        return JsonResponse(response_data)   
    return render(request,template_name) 


class DeleteCrudProductos(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        Productos.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
    
def Productos_visualizar(request,id):
    template_name = "Visualizar_productos.html"
    producto=Productos.objects.get(id=id)
    color=Color.objects.filter(est_color=True)
    categoria=Categorias.objects.filter(est_cat=True)
    proveedor=Proveedores.objects.filter(est_prov=True)
    marca=Marca.objects.filter(est_marca=True)
    presentacion=Presentacion.objects.filter(est_pre=True)

    #Seleccionado el color para mostrarla en el Combo
    colors=Color.objects.get(id=producto.color_prod.id)
    categorias=Categorias.objects.get(id=producto.cat_prod.id)
    proveedores=Proveedores.objects.get(id=producto.prov_prod.id)
    marcas=Marca.objects.get(id=producto.marca_prod.id)
    presentacions=Presentacion.objects.get(id=producto.present_prod.id)
    
    context = {"productos":producto,
               "Colores":color,
               "Categorias":categoria,
               "Proveedores":proveedor,
               "Marcas":marca,
               "Presentacion":presentacion,
               "colorseleccionado":colors.nom_color,
               "categoriaseleccionado":categorias.nom_cat,
               "proveedorseleccionado":proveedores.nom_prov,
               "marcaseleccionado":marcas.nom_marca,
               "presentacionseleccionado":presentacions.nom_pre
               }
    return render(request, template_name,context)    

def UpdateCrudProductos(request):
    response_data = {}
    template_name="Visualizar_productos.html"
    if request.POST.get('action') =='actualizar_productos':
        try:
            id=request.POST.get('id')
            productos = Productos.objects.get(id=id)
            productos.nom_prod=request.POST.get('txtnomprod')
            productos.cod_barra_prod=request.POST.get('txtcodbarra')
            productos.nom_etiqueta_prod=request.POST.get('txtetiqueta')
            productos.des_prod=request.POST.get('txtdescripcion')
            productos.umedida_prod=request.POST.get('txtumedida')
            productos.ubicacion=request.POST.get('txtubicacion')
            color_producto = request.POST.get('cmbcolor')
            if color_producto=="":
                color=productos.color_prod
            else:
                color=Color.objects.get(id=color_producto)
            productos.color_prod=color

            categoria_producto = request.POST.get('cmbcategoria')
            
            if categoria_producto=="":
                categoria=productos.cat_prod
            else:
                categoria=Categorias.objects.get(id=categoria_producto)
            productos.cat_prod=categoria
            
            proveedor_producto = request.POST.get('cmbproveedores')
            if proveedor_producto =="":
                provee=productos.prov_prod
            else:    
                provee=Proveedores.objects.get(id=proveedor_producto)
            productos.prov_prod=provee
            

            marca_producto = request.POST.get('cmbmarca')
            if marca_producto=="":
                marca=productos.marca_prod
            else:
                marca=Marca.objects.get(id=marca_producto)
            productos.marca_prod=marca

            presentacion_producto = request.POST.get('cmbpresentacion')
            if presentacion_producto=="":
                presentacion=productos.present_prod
            else:
                presentacion=Presentacion.objects.get(id=presentacion_producto)
            productos.present_prod=presentacion

            file = request.FILES.get('imgprod')
            if file:
                productos.img_prod=file

            productos.save()
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No Se Modifico el Productos Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Modifico con exito el Producto'  
            
             
        return JsonResponse(response_data)   
    return render(request,template_name) 
