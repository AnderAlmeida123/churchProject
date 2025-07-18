from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TipoSacramentoViewSet

router = DefaultRouter()
router.register('', TipoSacramentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
