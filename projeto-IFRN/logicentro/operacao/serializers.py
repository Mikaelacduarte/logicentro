from rest_framework import serializers
from operacao.models import Operacao

class OperacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operacao
        fields = '__all__'