from django.contrib import admin
from .models import TipoSacramento


@admin.register(TipoSacramento)
class TipoSacramentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'criado_em', 'atualizado_em')
    search_fields = ('nome', 'descricao')
    list_filter = ('nome', 'descricao')
