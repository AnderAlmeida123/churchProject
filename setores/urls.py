from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SetorViewSet

router = DefaultRouter()
router.register('setor', SetorViewSet)

urlpatterns = [
    path('',include(router.urls))
]