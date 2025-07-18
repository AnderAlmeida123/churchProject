from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from calendarios.models import Calendario
from calendarios.serializers import CalendarioSerializer
from calendarios.filters import CalendarioFilterClass

class CalendarioViewSet(viewsets.ModelViewSet):
    queryset = Calendario.objects.all()
    serializer_class = CalendarioSerializer
    rql_filter_class = CalendarioFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(responsavel=self.request.user)
        return qs
