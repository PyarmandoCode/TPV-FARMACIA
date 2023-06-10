from django.shortcuts import render
from .models import Categorias,Color,Proveedores,Tipo_Proveedor
from django.http import JsonResponse
from django.views.generic import  View

def index(request):
    template_name = "Index.html"
    return render(request, template_name)

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

