from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import TipoEventoViewSet

router = DefaultRouter()
router.register('', TipoEventoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
