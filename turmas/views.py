from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import Turma
from .serializers import TurmaSerializer
from .filters import TurmaFilterClass


class TurmaViewSet(viewsets.ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer
    rql_filter_class = TurmaFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(responsavel=self.request.user)
        return qs
