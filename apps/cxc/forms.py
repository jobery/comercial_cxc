from django import forms
from .models import *

class ClienteForm(forms.ModelForm):
    class Meta():
        model = Cliente
        fields = ['nombre','dui','direccion','telefono','email',]

class CargoForm(forms.ModelForm):
    class Meta():
        model = Cargo
        fields = [
            'cliente',
            'fecha',
            'documento',
            'val_cargo',]