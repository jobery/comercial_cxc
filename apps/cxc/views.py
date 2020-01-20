from django.shortcuts import render,redirect
from django.views.generic import CreateView,UpdateView,DeleteView,ListView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from decimal import Decimal

from .models import *
from .forms import *
# Create your views here.

class CreateCliente(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cxc/cliente/crearcliente.html'
    success_url = reverse_lazy('listarcliente')

class ListCliente(ListView):
    model = Cliente
    template_name = 'cxc/cliente/listarcliente.html'    

class UpdateCliente(UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cxc/cliente/editarcliente.html'
    success_url = reverse_lazy('listarcliente')

class DeleteCliente(DeleteView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'cxc/cliente/eliminarcliente.html'
    success_url = reverse_lazy('listarcliente')

class ListCargo(ListView):
    model = Cargo
    template_name = 'cxc/cargo/listarcargo.html'    

class CreateCargo(CreateView):
    model = Cargo
    form_class = CargoForm
    template_name = 'cxc/cargo/crearcargo.html'
    success_url = reverse_lazy('listarcargo')

    def post(self,request,*agrs,**kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        if form.is_valid():
            form.instance.val_saldo = form.instance.val_cargo
            form.save()
            return HttpResponseRedirect(self.get_success_url())                        
        else:
            return self.render_to_response(self.get_context_data(form=form))

class UpdateCargo(UpdateView):  
    model = Cargo
    form_class = CargoForm
    template_name = 'cxc/cargo/editarcargo.html'
    success_url = reverse_lazy('listarcargo')

class DeleteCargo(DeleteView):
    model = Cargo
    form_class = CargoForm
    template_name = 'cxc/cargo/eliminarcargo.html'
    success_url = reverse_lazy('listarcargo')

class ListAbono(ListView):
    model = Abono
    template_name = 'cxc/abono/listarabono.html'

class CreateAbono(CreateView):
    model = Abono
    form_class = AbonoForm
    template_name = 'cxc/abono/crearabono.html'
    success_url = reverse_lazy('listarabono')

    def post(self, request,*args,**kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form_cargo = Cargo.objects.get(pk=request.POST['cargo'])
        if form.is_valid():
            form_cargo.val_abono = form_cargo.val_abono + form.instance.val_abono
            form_cargo.val_saldo = form_cargo.val_saldo - form.instance.val_abono
            form_cargo.save()
            form.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

class UpdateAbono(UpdateView):
    model = Abono
    form_class = AbonoForm
    template_name = 'cxc/abono/editarabono.html'
    success_url = reverse_lazy('listarabono')    

class DeleteAbono(DeleteView):
    model = Abono
    form_class = AbonoForm
    template_name = 'cxc/abono/eliminarabono.html'
    success_url = reverse_lazy('listarabono')

    # def post(self,request,*args,**kwargs):
    #     self.object = self.get_object
    #     form = self.form_class(request.POST)



# class CreateAbonos(CreateView):
#     model = Abono
#     template_name = 'cxc/abono/crearabono.html'
#     form_class = AbonoForm
#     seccond_form_class = CargoForm
#     sucess_url = reverse_lazy('listarabono')

#     def get_context_data(self,**kwargs):
#         context = super(CreateAbonos,self).get_context_data(**kwargs)
#         if 'form' not in context:
#             context['form'] = self.form_class(self.request.GET)
#         if 'form2' not in context:
#             context['form2'] = self.seccond_form_class(self.request.GET)
#         return context

#     def post(self,request,*args,**kwargs):
#         self.object = self.get_object
#         form = self.form_class(request.POST)
#         form2 = self.seccond_form_class(request.POST)
#         if form.is_valid() and form2.is_valid():
#             abono = form.save(commit = False)
#             abono.cargo = form2.save()
#             abono.save()
#             return HttpResponseRedirect(self.get_success_url())
#         else:
#             return self.render_to_response(self.get_context_data(form=form,form2=form2))


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
    return render(request,'cxc/cliente/crearcliente.html',context)

def ListaCliente(request):
    cliente = Cliente.objects.all()
    context = {'clientes':cliente}
    return render(request,'cxc/cliente/listacliente.html',context)

def EditarCliente(request,id):
    cliente = Cliente.objects.get(id= id)
    if request.method == 'GET':
        form = ClienteForm(instance = cliente)
    else:
        form = ClienteForm(request.POST,instance = cliente)
        if form.is_valid():
            form.save()
        return redirect('listacliente')
    return render(request,'cxc/cliente/crearcliente.html',{'form':form})

def EliminarCliente(request,id):
    cliente = Cliente.objects.get(id = id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('listacliente')
    return render(request,'cxc/cliente/eliminarcliente.html',{'cliente':cliente})
