#Esse código cria um serializer para o modelo Motorista, permitindo a conversão entre instâncias do modelo e representações JSON, incluindo todos os campos do modelo.

from rest_framework import serializers
from motorista.models import Motorista

class MotoristaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Motorista
        fields = '__all__'