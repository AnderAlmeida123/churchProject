from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import SetorViewSet

router = DefaultRouter()
router.register('', SetorViewSet)

urlpatterns = router.urls
