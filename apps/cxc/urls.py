from django.urls import path

from .views import Home,CrearCliente,ListaCliente,EditarCliente

urlpatterns = [
    path('',Home,name='index'),
    path('crearcliente/',CrearCliente,name='crearcliente'),
    path('listacliente/',ListaCliente,name='listacliente'),
    path('editarcliente/<int:id>',EditarCliente,name='editarcliente'),
]
