from django.urls import path

#from .views import Home,CrearCliente,ListaCliente,EditarCliente,EliminarCliente
from .views import *

urlpatterns = [
    path('crearusuario/',CrearUsuario.as_view(),name='crearusuario'),
]