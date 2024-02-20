from django import forms
from .models import *

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['username', 'rut', 'email', 'direccion', 'celular', 'foto']