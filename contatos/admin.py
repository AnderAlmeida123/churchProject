from django.contrib import admin
from .models import Contato
from .forms import ContatoAdminForm


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    form = ContatoAdminForm
    list_display = (
        'id',
        'celular_formatado',
        'telefone_formatado',
        'email',
        'pessoa',
        'criado_em',
        'atualizado_em'
    )
    search_fields = ('celular', 'telContato', 'email', 'responsavel__username', 'pessoa__nome')
    list_filter = ('responsavel','pessoa__nome')
