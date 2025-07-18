from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CalendarioViewSet

router = DefaultRouter()
router.register('', CalendarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
