from django.shortcuts import render
from .models import Categorias
from django.http import JsonResponse

def index(request):
    template_name = "home\\Index.html"
    return render(request, template_name)

def categorias_listado(request):
    categorias = Categorias.objects.filter(est_cat=True)
    context = {
        "Categorias": categorias
    }
    template_name = "home\\Listado_categorias.html"
    return render(request, template_name, context)

def categoria_form(request):
    template_name = "home\\Nueva_categoria.html"
    return render(request, template_name)

def categoria_registrar(request):
    response_data = {}
    template_name="home\\Nueva_categoria.html"
    if request.POST.get('action') =='registrar_categoria':
        try:
            nombre_categoria = request.POST.get('txtnomcat')
            descripcion_categoria = request.POST.get('txtdescripcion')
            color_categoria = request.POST.get('cmbcolor')
            Categorias.objects.create(nom_cat=nombre_categoria,des_cat=descripcion_categoria,color_cat=color_categoria)
        except Exception as error:
            response_data['flag'] = False
            response_data['msg'] = f'No se Registro la Categoria Correctamente {error}'
        else:
            response_data['flag'] = True
            response_data['msg'] = 'Se Registro con exito la Categoria'   
        return JsonResponse(response_data)   
    return render(request,template_name) 

    

            



