from rest_framework import serializers
from .models import MembroSetor


class MembroSetorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembroSetor
        fields = '__all__'
        read_only_fields = ['responsavel']