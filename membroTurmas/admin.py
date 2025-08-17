from django.contrib import admin
from .models import MembroTurma
from .forms import MembroTurmaForm


@admin.register(MembroTurma)
class MembroTurmaAdmin(admin.ModelAdmin):
    form = MembroTurmaForm

    list_display = (
        'id',
        'pessoa',
        'turma',
        'data_entrada',
        'data_saida',
        'atualizado_em',
        'criado_em',
        'responsavel'
    )

    search_fields = ['pessoa__nome', 'turma__nome']
    list_filter = ('turma', 'data_entrada', 'data_saida', 'pessoa','turma__nome_turma')
