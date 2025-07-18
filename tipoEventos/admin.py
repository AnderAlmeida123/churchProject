from django.contrib import admin
from .models import TipoEvento


@admin.register(TipoEvento)
class TipoEventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_Evento', 'descricao', 'criado_em', 'atualizado_em')
    search_fields = ('nome_Evento', 'descricao')
    list_filter = ('nome_Evento', 'descricao')
