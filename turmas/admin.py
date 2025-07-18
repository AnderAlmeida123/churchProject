from django.contrib import admin
from .models import Turma


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'descricao', 'pessoa', 'responsavel', 'criado_em', 'atualizado_em')
    search_fields = ('nome', 'descricao', 'pessoa', 'responsavel__username')
    list_filter = ('nome', 'descricao', 'pessoa')
