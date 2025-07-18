from django import forms
from .models import Calendario


class CalendarioAdminForm(forms.ModelForm):
    class Meta:
        model = Calendario
        fields = '__all__'

    class Media:
        js = (
            'calendarios/js/jquery.mask.min.js',
            'calendarios/js/mask_calendario.js',
        )
