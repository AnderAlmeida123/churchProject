from rest_framework import serializers
from .models import Tesouraria


class TesourariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tesouraria
        fields = '__all__'
        read_only_fields = ['responsavel']