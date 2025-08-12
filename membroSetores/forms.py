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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['setor'].label_from_instance = lambda obj: obj.nome_setor  # 👈 ESSA LINHA RESOLVE

    class Media:
        js = (
            'membroSetores/js/jquery.mask.min.js',
            'membroSetores/js/mask_membroSetor.js',
        )
