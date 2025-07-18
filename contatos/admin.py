from django.contrib import admin
from contatos.models import Contato
from .forms import ContatoAdminForm


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    form = ContatoAdminForm
    list_display = (
        'id',
        'celular_formatado',
        'telefone_formatado',
        'email',
        'criado_em',
        'atualizado_em'
    )
    search_fields = ('celular', 'telContato', 'email', 'responsavel__username')
    list_filter = ('responsavel',)
