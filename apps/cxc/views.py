from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy

from .models import *
from .forms import *
# Create your views here.

class CreateCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/crearcliente.html'
    success_url = reverse_lazy('listarcliente')

class ListCliente(ListView):
    model = Cliente
    template_name = 'cliente/listarcliente.html'    

class UpdateCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/editarcliente.html'
    success_url = reverse_lazy('listarcliente')

class DeleteCliente(DeleteView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/eliminarcliente.html'
    success_url = reverse_lazy('listarcliente')

class ListCargo(ListView):
    model = Cargo
    template_name = 'cargo/listarcargo.html'    

class CreateCargo(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'cargo/crearcargo.html'
    success_url = reverse_lazy('listarcargo')

class UpdateCargo(UpdateView):  
    model = Cargo
    form_class = CargoForm
    template_name = 'cargo/editarcargo.html'
    success_uls = reverse_lazy('listarcargo')

class DeleteCargo(DeleteView):
    model = Cargo
    form_class = CargoForm
    template_name = 'cargo/eleminarcargo.html'
    success_url = reverse_lazy('listarcargo')


def index(request):
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
        form = ClienteForm(instance = cliente)
    else:
        form = ClienteForm(request.POST,instance = cliente)
        if form.is_valid():
            form.save()
        return redirect('listacliente')
    return render(request,'cliente/crearcliente.html',{'form':form})

def EliminarCliente(request,id):
    cliente = Cliente.objects.get(id = id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listacliente')
    return render(request,'cliente/eliminarcliente.html',{'cliente':cliente})
