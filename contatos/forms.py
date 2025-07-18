from django import forms
from .models import Contato


class ContatoAdminForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'

    class Media:
        js = (
            'contatos/js/jquery.mask.min.js',
            'contatos/js/mask_contato.js',
        )
