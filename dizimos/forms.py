from decimal import Decimal
from django import forms
from .models import Dizimo

class DizimoAdminForm(forms.ModelForm):
    valor = forms.CharField(label='Valor')

    mes = forms.ChoiceField(
        choices=Dizimo.MESES_DO_ANO,
        label="Mês"
    )

    tipo_pagamento = forms.ChoiceField(
        choices=Dizimo.TIPOS_PAGAMENTO,
        label="Tipo de Pagamento"
    )

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
