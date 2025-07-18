from rest_framework import serializers
from dizimos.models import Dizimo


class DizimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dizimo
        fields = '__all__'
        read_only_fields = ['responsavel']