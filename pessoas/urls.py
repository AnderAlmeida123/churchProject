from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PessoaViewSet

router = DefaultRouter()
router.register(r'', PessoaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
