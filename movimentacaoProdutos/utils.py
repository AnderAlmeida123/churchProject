from django.db.models import Sum
from .models import MovimentacaoProduto

def calcular_estoque_produto(produto_id):
    entradas = MovimentacaoProduto.objects.filter(
        produto_id=produto_id, tipo=MovimentacaoProduto.ENTRADA
    ).aggregate(total=Sum('quantidade'))['total'] or 0

    saidas = MovimentacaoProduto.objects.filter(
        produto_id=produto_id, tipo=MovimentacaoProduto.SAIDA
    ).aggregate(total=Sum('quantidade'))['total'] or 0

    return entradas - saidas
