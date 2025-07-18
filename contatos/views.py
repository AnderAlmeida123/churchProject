from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions, IsAdminUser
from contatos.models import Contato
from contatos.serializers import ContatoSerializer
from contatos.filters import ContatoFilterClass


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
    rql_filter_class = ContatoFilterClass
    permission_classes = (DjangoModelPermissions, IsAdminUser,)

    def perform_create(self, serializer):
        serializer.save(responsavel=self.request.user)

    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_staff:
            qs = qs.filter(responsavel=self.request.user)
        return qs