from django import forms
from .models import Contato

class ContatoAdminForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
        widgets = {
            'celular': forms.TextInput(attrs={'class': 'contato-mask'}),
            'telContato': forms.TextInput(attrs={'class': 'contato-mask'}),
        }

    class Media:
        js = (
            'contatos/js/jquery.mask.min.js',
            'contatos/js/mask_contato.js',
        )

    def save(self, *args, **kwargs):
        # Limpa caracteres que não sejam dígitos antes de salvar
        celular = self.cleaned_data.get('celular', '')
        tel = self.cleaned_data.get('telContato', '')
        self.instance.celular = ''.join(filter(str.isdigit, celular))
        self.instance.telContato = ''.join(filter(str.isdigit, tel))
        return super().save(*args, **kwargs)
