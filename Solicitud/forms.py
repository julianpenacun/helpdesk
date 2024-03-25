from django import forms
from .models import Solicitudes

class FormularioSolicitudes(forms.ModelForm):
    class Meta:
        model = Solicitudes
        fields = [
            'titulo',
            'descripcion',
            'urgente',
        ]
        
        widgets = {

            'titulo': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Write a title'}),
            'descripcion': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Write a description'}),
            'urgente': forms.CheckboxInput(attrs={'class':'form-check-input m-auto'}),

        }