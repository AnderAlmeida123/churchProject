from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import MembroTurma
from .serializers import MembroTurmaSerializer
from .filters import MembroTurmaFilterClass


class MembroTurmaViewSet(viewsets.ModelViewSet):
    queryset = MembroTurma.objects.all()
    serializer_class = MembroTurmaSerializer
    rql_filter_class = MembroTurmaFilterClass
    permission_classes = (DjangoModelPermissions, IsAdminUser)

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(responsavel=self.request.user)
        return qs
