from django import forms
from .models import Pessoa


class PessoaAdminForm(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'
        widgets = {
            'cpf': forms.TextInput(attrs={'class': 'cpf-mask'}),
            'data_nascimento': forms.TextInput(attrs={'class': 'data_nascimento-mask'}),
        }

    class Media:
        js = (
            'pessoas/js/jquery.mask.min.js',
            'pessoas/js/mask_pessoa.js',
        )