from rest_framework import serializers
from .models import MovimentacaoProduto
from .utils import calcular_estoque_produto

class MovimentacaoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovimentacaoProduto
        fields = '__all__'


# Retorna o saldo de um produto específico
class EstoqueSerializer(serializers.Serializer):
    produto_id = serializers.IntegerField()
    saldo = serializers.IntegerField()
