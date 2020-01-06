from django.urls import path

#from .views import Home,CrearCliente,ListaCliente,EditarCliente,EliminarCliente
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('crearcliente/',CreateCliente.as_view(),name='crearcliente'),
    path('listarcliente/',ListCliente.as_view(),name='listarcliente'),
    path('editarcliente/<int:pk>',UpdateCliente.as_view(),name='editarcliente'),
    path('eliminarcliente/<int:pk>',DeleteCliente.as_view(),name='eliminarcliente'),
]
