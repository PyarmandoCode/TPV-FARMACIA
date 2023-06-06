from django.shortcuts import render
from .models import Categorias,Color
from django.http import JsonResponse
from django.views.generic import  View

def index(request):
    template_name = "home\\Index.html"
    return render(request, template_name)

def Categorias_listado(request):
    categorias = Categorias.objects.filter(est_cat=True)
    context = {
        "Categorias": categorias,
    }
    template_name = "home\\Listado_categorias.html"
    return render(request, template_name, context)

def Categoria_visualizar(request,id):
    template_name = "home\\Visualizar_categoria.html"
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
    template_name = "home\\Nueva_categoria.html"
    return render(request, template_name,context)

def CreateCrudCategorias(request):
    response_data = {}
    template_name="home\\Nueva_categoria.html"
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
    template_name="home\\Visualizar_categoria.html"
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
            categoria.save()
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No Se Modifico la Categoria Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Modifico con exito la Categoria'  
            
             
        return JsonResponse(response_data)   
    return render(request,template_name) 


            



