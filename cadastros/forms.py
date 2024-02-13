from django import forms
from .models import Bolos

class boloForm(forms.ModelForm):
    class Meta:
        model= Bolos
        fields = ('nome', 'descricao', 'tamanho', 'observacao', 'sabor')