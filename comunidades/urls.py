from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ComunidadeViewSet

router = DefaultRouter()
router.register(r'', ComunidadeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
