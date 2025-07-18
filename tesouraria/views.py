from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import Tesouraria
from .filters import TesourariaFilter
from .serializers import TesourariaSerializer


class TesourariaViewSet(viewsets.ModelViewSet):
    queryset = Tesouraria.objects.all()
    serializer_class = TesourariaSerializer
    rql_filter_class = TesourariaFilter
    permission_classes = [DjangoModelPermissions, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(responsavel=self.request.user)
        return qs
