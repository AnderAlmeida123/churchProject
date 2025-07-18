from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import TipoSacramento
from .serializers import TipoSacramentoSerializer
from .filters import TipoSacramentoFilterClass

class TipoSacramentoViewSet(viewsets.ModelViewSet):
    queryset = TipoSacramento.objects.all()
    serializer_class = TipoSacramentoSerializer
    rql_filter_class = TipoSacramentoFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(responsavel=self.request.user)
        return qs
