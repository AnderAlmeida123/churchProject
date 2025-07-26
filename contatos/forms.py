from django import forms
from .models import Contato

class ContatoAdminForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        widgets = {
            'celular': forms.TextInput(attrs={'class': 'contato-mask'}),
            'telContato': forms.TextInput(attrs={'class': 'contato-mask'}),
        }

    class Media:
        js = (
            'contatos/js/jquery.mask.min.js',
            'contatos/js/mask_contato.js',
        )
