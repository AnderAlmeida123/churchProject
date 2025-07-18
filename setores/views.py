from rest_framework import viewsets
from .models import Setor
from .serializers import SetorSerializer


class SetorViewSet(viewsets.ModelViewSet):
    queryset = Setor.objects.all()
    serializer_class = SetorSerializer
