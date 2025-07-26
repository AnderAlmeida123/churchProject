from django import forms
from .models import MembroTurma


class MembroTurmaForm(forms.ModelForm):
    class Meta:
        model = MembroTurma
        fields = '__all__'
        widgets = {
            'data_entrada': forms.TextInput(attrs={'class': 'data-mask'}),
            'data_saida': forms.TextInput(attrs={'class': 'data-mask'}),
        }

    class Media:
        js = (
            'membroTurmas/js/jquery.mask.min.js',
            'membroTurmas/js/mask_membroTurma.js',
        )
