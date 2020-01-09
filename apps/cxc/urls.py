from django.urls import path

#from .views import Home,CrearCliente,ListaCliente,EditarCliente,EliminarCliente
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('crearcliente/',CreateCliente.as_view(),name='crearcliente'),
    path('listarcliente/',ListCliente.as_view(),name='listarcliente'),
    path('editarcliente/<int:pk>',UpdateCliente.as_view(),name='editarcliente'),
    path('eliminarcliente/<int:pk>',DeleteCliente.as_view(),name='eliminarcliente'),    
    path('listarcargo/',ListCargo.as_view(),name='listarcargo'),
    path('crearcargo/',CreateCargo.as_view(),name='crearcargo'),
    path('editarcargo/<int:pk>',UpdateCargo.as_view(),name='editarcargo'),
    path('eliminarcargo/<int:pk>',DeleteCargo.as_view(),name='eliminarcargo'),
]
