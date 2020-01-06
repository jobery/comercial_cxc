from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy

from .models import Cliente
from .forms import ClienteForm
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
