from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import UsuarioForm
# Create your views here.

class CrearUsuario(CreateView):
    model = User
    template_name = 'usuario/crearusuario.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('index')

