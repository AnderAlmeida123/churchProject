from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from .models import Endereco
from .serializers import EnderecoSerializer
from .filters import EnderecoFilterClass


class EnderecoViewSet(viewsets.ModelViewSet):
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    rql_filter_class = EnderecoFilterClass
    permission_classes = [DjangoModelPermissions, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(responsavel=self.request.user)
        return qs
