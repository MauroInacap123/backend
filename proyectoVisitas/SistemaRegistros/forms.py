from django import forms
from .models import Visita

# Formulario para crear o editar una visita
class VisitaForm(forms.ModelForm):
    # Definimos los metadatos del formulario
    class Meta:
        # Especificamos el modelo asociado a este formulario
        model = Visita
        
        # Especificamos los campos que serán utilizados en el formulario
        fields = ["rut", "nombre", "motivo_visita", "fecha_visita", "hora_entrada", "hora_salida"]

        # Los campos de 'rut', 'nombre', 'motivo_visita', 'fecha_visita', 'hora_entrada', 'hora_salida'
        # seran los que se van a mostrar en el formulario.
