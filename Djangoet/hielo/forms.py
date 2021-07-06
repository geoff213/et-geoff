from django import forms
from django.forms import ModelForm, widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Colaboradores


class ColaboradoresForm(forms.ModelForm):

    class Meta:
        model = Colaboradores
        fields = ['Rut','Image','NombreCompleto','Telefono','Direccion','Email','Contrasenia','pais']

        labels={
            'Rut': 'rut',
            'Image': 'Imagen',
            'NombreCompleto': 'Nombre_Completo',
            'Telefono': 'Telefono',
            'Direccion': 'Direccion',
            'Email': 'Email',
            'contrasenia': 'Contraseña',
            'Pais': 'pais',
        }
        
        widgets={
            'Rut': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'rut',
                    'name': 'rut',
                    'type': 'text',
                    'placeholder': 'Ingrese su Rut'
                }
            ),
            'NombreCompleto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'nombre',
                    'name': 'nombre',
                    'type': 'text',
                    'placeholder': 'Nombre completo:'
                }
            ),
            'Image': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'foto',
                    'name': 'foto',
                    'type': 'file',
                    'placeholder': 'Adjuntar foto'
                }
            ),
            'Email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'email',
                    'name': 'email',
                    'type': 'text',
                    'placeholder': 'Email: '
                }
            ),
            'Telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'fono',
                    'name': 'fono',
                    'type': 'number',
                    'placeholder': 'Telefono: '
                }
            ),
            'Contrasenia': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'contra',
                    'name': 'contra',
                    'type': 'password',
                    'placeholder': 'Contraseña: '
                }
            ),
            'Direccion': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'direccion',
                    'name': 'direccion',
                    'type': 'text',
                    'placeholder': 'Ingrese su Direccion'
                }
            ),
            'Pais': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'id': 'rut',
                    'name': 'rut',
                    'type': 'text',
                    'placeholder': 'Ingrese su Rut'
                }
            ),
        }