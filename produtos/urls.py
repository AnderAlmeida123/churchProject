from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProdutoViewSet

router = DefaultRouter()
router.register('', ProdutoViewSet)

urlpatterns = router.urls
