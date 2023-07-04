from django import forms
from .models import Especialidad, SoporteTI, Ticket

class EspecialidadForm(forms.ModelForm):
    class Meta:
        model = Especialidad
        fields = ['nombre']
        labels = {
            'nombre': 'Nombre de especialidad'
        }

class SoporteForm(forms.ModelForm):
    class Meta:
        model = SoporteTI
        fields = ['nombre', 'especialidades', 'imagen_perfil']
        labels = {
            'nombre': 'Nombre de soporte',
            'especialidades': 'Especialidades',
            'imagen_perfil': 'Imagen de perfil'
        }
        widgets = {
            'especialidades': forms.CheckboxSelectMultiple()
        }

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titulo', 'descripcion', 'soporte']
        labels = {
            'titulo': 'Título del ticket',
            'descripcion': 'Descripción del ticket',
            'soporte': 'Soporte'
        }
        widgets = {
            'soporte': forms.Select()
        }
