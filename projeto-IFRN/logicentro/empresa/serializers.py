from rest_framework import serializers
from empresa.models import Empresa

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'
        
    # O código cria um serializer para o modelo Empresa, que permite converter instâncias desse modelo em dados JSON que podem ser enviados como resposta em uma API, além de permitir a validação e a transformação de dados JSON recebidos em objetos do modelo Empresa ao criar ou atualizar registros. 
    # A utilização de fields = '__all__' significa que todos os campos definidos no modelo Empresa serão incluídos nas operações de serialização