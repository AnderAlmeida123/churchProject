from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import Setor
from .serializers import SetorSerializer
from .filters import SetorFilterClass


class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
    rql_filter_class = SetorFilterClass
    permission_classes = (DjangoModelPermissions, IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(responsavel=self.request.user)
        return qs