from django.contrib import admin
from .models import Produto
from movimentacaoProdutos.utils import calcular_estoque_produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'mostrar_estoque', 'ativo')
    search_fields = ('nome', 'categoria')

    def mostrar_estoque(self, obj):
        return calcular_estoque_produto(obj.id)

    mostrar_estoque.short_description = 'Estoque Atual'
