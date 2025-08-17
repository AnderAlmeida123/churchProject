from django.contrib import admin
from .forms import SetorAdminForm
from .models import Setor


@admin.register(Setor)
class SetorAdmin(admin.ModelAdmin):
    form = SetorAdminForm
    list_display = (
        'nome_setor',
        'descricao',
        'criado_em',
        'atualizado_em'
    )
    search_fields = ('nome_setor','responsavel__username')
    list_filter = ('responsavel','nome_setor')