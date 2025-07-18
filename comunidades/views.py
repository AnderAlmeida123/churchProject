from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import Comunidade
from .serializers import ComunidadeSerializer
from .filters import ComunidadeFilterClass


class ComunidadeViewSet(viewsets.ModelViewSet):
    queryset = Comunidade.objects.all()
    serializer_class = ComunidadeSerializer
    rql_filter_class = ComunidadeFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(responsavel=self.request.user)
        return qs
