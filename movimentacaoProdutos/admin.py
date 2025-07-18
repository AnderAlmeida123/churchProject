from django.contrib import admin
from .models import MovimentacaoProduto

@admin.register(MovimentacaoProduto)
class MovimentacaoProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo', 'produto', 'quantidade', 'setor_destino', 'responsavel', 'criado_em')
    search_fields = ('produto__nome', 'setor_destino__nome')
    list_filter = ('tipo', 'produto', 'setor_destino')
