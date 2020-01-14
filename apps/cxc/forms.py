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
        widgets = {
            'cliente': forms.Select(attrs={'class':'form-control'}),
            'fecha': forms.DateInput(attrs={'class':'form-control','type':'date'},format='%Y-%m-%d'),
            'documento': forms.TextInput(attrs={'class':'form-control',}),
            'val_cargo': forms.NumberInput(attrs={'class':'form-control',}),
        }

class AbonoForm(forms.ModelForm):
    class Meta():
        model = Abono
        fields = [
            'cargo',
            'fecha',
            'val_abono',
        ]
        labels = {
            'cargo':'Cargo',
            'fecha':'Fecha',
            'val_abono':'Abono',
        }        
        widgets = {
            'cargo': forms.Select(attrs={'class':'form-control',}),
            'fecha': forms.DateInput(attrs={'type':'date','class':'form-control',},format='%Y-%m-%d'),
            'val_abono': forms.NumberInput(attrs={'class':'form-control',}),
        }