from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MembroSetorViewSet

router = DefaultRouter()
router.register(r'', MembroSetorViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
