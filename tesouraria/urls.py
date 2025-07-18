from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TesourariaViewSet

router = DefaultRouter()
router.register(r'', TesourariaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
