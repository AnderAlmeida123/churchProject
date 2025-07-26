from django import forms
from .models import MembroSetor


class MembroSetorForm(forms.ModelForm):
    class Meta:
        model = MembroSetor
        fields = '__all__'
        widgets = {
            'data_entrada': forms.TextInput(attrs={'class': 'data-mask'}),
            'data_saida': forms.TextInput(attrs={'class': 'data-mask'}),
        }

    class Media:
        js = (
            'membroSetores/js/jquery.mask.min.js',
            'membroSetores/js/mask_membroSetor.js',
        )