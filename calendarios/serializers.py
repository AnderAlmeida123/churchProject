from rest_framework import serializers
from .models import Calendario


class CalendarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendario
        fields = '__all__'
        read_only_fields = ['responsavel']
