from django.shortcuts import render,redirect
from django.views.generic import ListView

from .models import Cliente
from .forms import ClienteForm
# Create your views here.

# class ClienteList(ListView):
#     model = Cliente
#     template_name = 'cliente/clientelist.html'

def Home(request):
    return render(request,'index.html')

def CrearCliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listacliente')
    else:
        form = ClienteForm()
        context = {'form':form}
    return render(request,'cliente/crearcliente.html',context)

def ListaCliente(request):
    cliente = Cliente.objects.all()
    context = {'clientes':cliente}
    return render(request,'cliente/listacliente.html',context)

def EditarCliente(request,id):
    cliente = Cliente.objects.get(id= id)
    if request.method == 'GET':
        form = Cliente(instance = cliente)
    else:
        form = ClienteForm(request.POST,instance = cliente)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request,'cliente/crearcliente.html',{'form':form})
