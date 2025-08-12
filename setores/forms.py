from django import forms
from .models import Setor


class SetorAdminForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = '__all__'


    class Media:
        js = (
            'setores/js/jquery.mask.min.js',
            'setores/js/mask_setor.js'
        )