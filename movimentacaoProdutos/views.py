from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MovimentacaoProduto
from .serializers import MovimentacaoProdutoSerializer, EstoqueSerializer
from .utils import calcular_estoque_produto

class MovimentacaoProdutoViewSet(viewsets.ModelViewSet):
    queryset = MovimentacaoProduto.objects.all()
    serializer_class = MovimentacaoProdutoSerializer

class EstoqueViewSet(APIView):
    def get(self, request, produto_id):
        saldo = calcular_estoque_produto(produto_id)
        data = {
            "produto_id": produto_id,
            "saldo": saldo
        }
        serializer = EstoqueSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
