from django import forms
from .models import Endereco


class EnderecoAdminForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = '__all__'

    class Media:
        js = (
            'enderecos/js/jquery.mask.min.js',
            'enderecos/js/mask_endereco.js',
        )
