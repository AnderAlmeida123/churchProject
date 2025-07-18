from django.contrib import admin
from .models import Tesouraria


@admin.register(Tesouraria)
class TesourariaAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_movimentacao', 'descricao', 'valor', 'data_movimentacao', 'entrada_saida', 'setor', 'responsavel', 'criado_em', 'atualizado_em')
    search_fields = ('tipo_movimentacao', 'descricao', 'data_movimentacao', 'entrada_saida')
    list_filter = ('tipo_movimentacao', 'descricao', 'entrada_saida', 'data_movimentacao', 'setor')