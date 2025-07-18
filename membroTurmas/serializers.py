from rest_framework import serializers
from .models import MembroTurma


class MembroTurmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembroTurma
        fields = '__all__'
        read_only_fields = ['responsavel']