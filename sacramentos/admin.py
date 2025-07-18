from django.contrib import admin
from .models import Sacramento


@admin.register(Sacramento)
class SacramentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'data_hora', 'tipo_sacramento', 'comunidade', 'responsavel', 'criado_em',
                    'atualizado_em')
    search_fields = ('pessoa', 'data_hora', 'tipo_sacramento', 'comunidade', 'responsavel__username')
    list_filter = ('pessoa', 'comunidade', 'data_hora', 'tipo_sacramento', 'responsavel__username')
