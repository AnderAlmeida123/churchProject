from django.urls import path, include
from rest_framework.routers import DefaultRouter
from contatos.views import (ContatoViewSet)

router = DefaultRouter()
router.register('contato', ContatoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]