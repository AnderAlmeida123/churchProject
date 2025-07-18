from decimal import Decimal
from django import forms
from .models import Dizimo


class DizimoAdminForm(forms.ModelForm):
    # ESSENCIAL: força o campo a ser 'text' no HTML
    valor = forms.CharField(label='Valor')

    class Meta:
        model = Dizimo
        fields = '__all__'

    def clean_valor(self):
        valor = self.cleaned_data.get('valor')

        if isinstance(valor, str):
            valor = valor.replace('.', '').replace(',', '.')
        try:
            return Decimal(valor)
        except:
            raise forms.ValidationError("Valor inválido.")

    class Media:
        js = (
            'dizimos/js/jquery.mask.min.js',
            'dizimos/js/mask_dizimo.js',
        )
