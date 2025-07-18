from django.urls import path, include
from rest_framework.routers import DefaultRouter
from dizimos.views import DizimoViewSet

router = DefaultRouter()
router.register(r'', DizimoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
