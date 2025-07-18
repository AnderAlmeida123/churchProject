from rest_framework import serializers
from .models import Setor


class SetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setor
        fields = '__all__'
        read_only_fields = ['responsavel']