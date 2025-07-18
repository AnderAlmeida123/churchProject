from rest_framework import serializers
from .models import TipoSacramento


class TipoSacramentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoSacramento
        fields = '__all__'

