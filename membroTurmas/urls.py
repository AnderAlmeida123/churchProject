from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MembroTurmaViewSet

router = DefaultRouter()
router.register(r'', MembroTurmaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
