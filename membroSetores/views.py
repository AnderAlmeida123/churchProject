from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import MembroSetor
from .serializers import MembroSetorSerializer
from .filters import MembroSetorFilterClass


class MembroSetorViewSet(viewsets.ModelViewSet):
    queryset = MembroSetor.objects.all()
    serializer_class = MembroSetorSerializer
    rql_filter_class = MembroSetorFilterClass
    permission_classes = (DjangoModelPermissions, IsAdminUser)

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(responsavel=self.request.user)
        return qs
