from django import forms
from .models import Tesouraria


class TesourariaAdminForm(forms.ModelForm):
    class Meta:
        model = Tesouraria
        fields = '__all__'
        widgets = {
            'valor': forms.TextInput(attrs={'class': 'valor-mask'}),
            'data_movimentacao': forms.TextInput(attrs={'class': 'data_movimentacao-mask'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['setor'].label_from_instance = lambda obj: obj.nome_setor  # 👈 ESSA LINHA RESOLVE

    class Media:
        js = (
            'tesouraria/js/jquery.mask.min.js',
            'tesouraria/js/mask_tesouraria.js'
        )
