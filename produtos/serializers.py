from rest_framework import serializers
from .models import Produto
from movimentacaoProdutos.utils import calcular_estoque_produto


class ProdutoSerializer(serializers.ModelSerializer):
    estoque = serializers.SerializerMethodField()

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'categoria', 'descricao', 'ativo', 'estoque']

    def get_estoque(self, obj):
        return calcular_estoque_produto(obj.id)
