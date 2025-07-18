from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import Sacramento
from .serializers import SacramentoSerializer
from .filters import SacramentoFilterClass


class SacramentoViewSet(viewsets.ModelViewSet):
    queryset = Sacramento.objects.all()
    serializer_class = SacramentoSerializer
    rql_filter_class = SacramentoFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(responsavel=self.request.user)
        return qs
