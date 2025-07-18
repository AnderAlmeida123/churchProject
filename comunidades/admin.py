from django.contrib import admin
from .models import Comunidade


@admin.register(Comunidade)
class ComunidadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_comunidade', 'bairro', 'responsavel', 'criado_em', 'atualizado_em')
    search_fields = ('nome_comunidade', 'bairro', 'responsavel__username')
    list_filter = ('nome_comunidade', 'bairro')
