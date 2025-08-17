from django.contrib import admin
from .models import Turma


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_turma', 'descricao', 'responsavel', 'criado_em', 'atualizado_em')
    search_fields = ('nome_turma', 'descricao','responsavel__username')
    list_filter = ('nome_turma', 'descricao')
