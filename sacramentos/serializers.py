from rest_framework import serializers
from .models import Sacramento


class SacramentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sacramento
        fields = '__all__'
        read_only_fields = ['responsavel']
