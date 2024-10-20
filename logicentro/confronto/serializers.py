from rest_framework import serializers
from confronto.models import Confronto
from operacao.serializers import OperacaoSerializer


class ConfrontoSerializer(serializers.ModelSerializer):
    operacao = OperacaoSerializer(read_only=True)
    class Meta:
        model = Confronto
        fields = '__all__'