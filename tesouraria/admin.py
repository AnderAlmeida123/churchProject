from django.contrib import admin
from .models import Tesouraria
from .forms import TesourariaAdminForm


@admin.register(Tesouraria)
class TesourariaAdmin(admin.ModelAdmin):
    form = TesourariaAdminForm
    list_display = ('id', 'tipo_movimentacao', 'descricao', 'valor', 'data_movimentacao', 'setor',
                    'responsavel', 'criado_em', 'atualizado_em')
    search_fields = ('tipo_movimentacao', 'descricao', 'data_movimentacao','setor__nome')
    list_filter = ('tipo_movimentacao', 'descricao', 'data_movimentacao', 'setor')
