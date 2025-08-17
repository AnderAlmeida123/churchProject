from rest_framework import serializers
from contatos.models import Contato


class ContatoSerializer(serializers.ModelSerializer):
    pessoa_nome = serializers.CharField(source='pessoa.nome', read_only=True)

    class Meta:
        model = Contato
        fields = '__all__'
        read_only_fields = ['responsavel']
