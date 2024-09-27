from django.shortcuts import render
from .models import Templeado
from .forms import EmpleadoappModelForm
# Create your views here.

def index_empleadoapp(request):
    empleadosapp_lista=Templeado.objects.alias()  
    context={
        'empleadosapp_lista':empleadosapp_lista
    }
    return render(request,'empleadoapp/lista.html',context)
    
def crear_empleadoapp(request):
    form=EmpleadoappModelForm()
    if request.method=='POST':
        form=EmpleadoappModelForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    context={
        'form':form
    }
    return render(request,'empleadoapp/crear.html',context)

def borrar_empleadoapp(request,pk):
    Templeado.objects.get(pk=pk).delete()
    return index_empleadoapp(request)