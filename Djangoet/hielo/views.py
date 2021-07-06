from django.shortcuts import render, redirect
from .forms import ColaboradoresForm
from .models import Colaboradores
# Create your views here.

def formulario(request):
    return render(request, 'formulario.html')
def uptown(request):
    return render (request, 'hielo/uptown.html')

def form_colabor(request):
    if request.method =='POST':
        colabara=ColaboradoresForm(request.POST)
        if colabara.is_valid():
            colabara.save()
            return redirect('formulario')
    else:
        colabara=ColaboradoresForm()
    return render(request, 'hielo/formulario.html', {'colabara': colabara})

def mostarcolab(request):
    col = Colaboradores.objects.all()
    return render(request, 'hielo/mostrar.html', context={'col':col})

def deleteColaborador(request,id):
    delete = Colaboradores.objects.get(rut=id)
    delete.delete()
    return redirect('mostrar')


def modColabo(request,id):
    modi = Colaboradores.objects.get(rut=id)

    datos ={
           'form': ColaboradoresForm(instance=modi)
    }
    if request.method == 'POST': 
        modif = ColaboradoresForm(data=request.POST, instance = modi)
        if modif.is_valid: 
            modif.save()          
            return redirect('mostrar') 
    return render(request, 'hielo/uptown.html', datos)

