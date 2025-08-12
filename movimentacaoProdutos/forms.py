from django import forms
from .models import MovimentacaoProduto


class MovimentacaoProdutoForm(forms.ModelForm):
    class Meta:
        model = MovimentacaoProduto
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['setor_destino'].label_from_instance = lambda obj: obj.nome_setor
