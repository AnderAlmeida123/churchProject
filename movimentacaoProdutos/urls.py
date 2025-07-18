from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MovimentacaoProdutoViewSet
from .views import EstoqueViewSet

router = DefaultRouter()
router.register(r'', MovimentacaoProdutoViewSet, basename='movimentacao-produto')

urlpatterns = [
    # rota do estoque que é uma APIView (não é ViewSet, então aqui tudo bem usar `as_view`)
    path('estoque/<int:produto_id>/', EstoqueViewSet.as_view(), name='estoque-produto'),
]

# adiciona as rotas do router
urlpatterns += router.urls
