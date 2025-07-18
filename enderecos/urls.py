from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import EnderecoViewSet

router = DefaultRouter()
router.register('', EnderecoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
