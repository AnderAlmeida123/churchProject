from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from dizimos.models import Dizimo
from dizimos.serialzers import DizimoSerializer
from dizimos.filters import DizimoFilterClass


class DizimoViewSet(viewsets.ModelViewSet):
    queryset = Dizimo.objects.all()
    serializer_class = DizimoSerializer
    rql_filter_class = DizimoFilterClass
    permission_classes = (DjangoModelPermissions, IsAdminUser)

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(responsavel=self.request.user)
        return qs
