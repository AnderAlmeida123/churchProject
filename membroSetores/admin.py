from django.contrib import admin
from .models import MembroSetor
from .forms import MembroSetorForm


@admin.register(MembroSetor)
class MembroSetorAdmin(admin.ModelAdmin):
    form = MembroSetorForm

    list_display = (
        'id',
        'pessoa',
        'setor',
        'data_entrada',
        'data_saida',
        'atualizado_em',
        'criado_em',
        'responsavel',
    )

    search_fields = ['pessoa__nome', 'setor__nome']
    list_filter = ('setor', 'data_entrada', 'data_saida', 'pessoa')
