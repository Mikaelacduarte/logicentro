from datetime import datetime

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from confronto.models import Confronto
from confronto.serializers import ConfrontoSerializer
from operacao.models import Operacao


# Create your views here.
class ConfrontoViewSet(viewsets.ModelViewSet):
    queryset = Confronto.objects.all()
    serializer_class = ConfrontoSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        # Receber o JSON
        data = request.data

        # Extrair os dados recebidos
        id_operacao = data.get('id_operacao')
        placa_veiculo = data.get('placa_veículo')
        nome_motorista = data.get('nome_motorista')
        nro_mdfe = data.get('nro_mdfe')
        nro_notafiscal = data.get('nro_notafiscal')
        nro_lacre = data.get('nro_lacre')

        # Lista para armazenar campos inconsistentes
        campos_inconsistentes = []

        # Busca a operação no banco de dados
        try:
            operacao = Operacao.objects.get(id_operacao=id_operacao)
        except Operacao.DoesNotExist:
            return Response({'error': 'Operação não encontrada.'}, status=status.HTTP_404_NOT_FOUND)

        # Verificar a placa do veículo
        if operacao.placa != placa_veiculo:
            campos_inconsistentes.append('placa_veículo')

        # Verificar o nome do motorista (buscando o nome do motorista da operação)
        if operacao.motorista.nome != nome_motorista:
            campos_inconsistentes.append('nome_motorista')

        # Verificar o nro_mdfe (opcional)
        if operacao.nro_mdfe is not None and operacao.nro_mdfe != nro_mdfe:
            campos_inconsistentes.append('nro_mdfe')

        # Verificar o nro_mdfe (opcional)
        if operacao.nro_mdfe is not None and operacao.nro_mdfe != nro_mdfe:
            campos_inconsistentes.append('nro_mdfe')

        # Verificar o nro_notafiscal (opcional)
        if operacao.nro_notafiscal is not None and operacao.nro_notafiscal != nro_notafiscal:
            campos_inconsistentes.append('nro_notafiscal')

        # Verificar o nro_lacre (opcional)
        if operacao.nro_lacre is not None and operacao.nro_lacre != nro_lacre:
            campos_inconsistentes.append('nro_lacre')

        # Definir o status do confronto com base nas inconsistências
        status_confronto = 'Concluído' if not campos_inconsistentes else 'Inconsistente'

        # Criar e salvar o confronto
        confronto = Confronto.objects.create(
            operacao=operacao,
            status=status_confronto
        )

        #atualizando o status da operação após o confronto
        operacao.status="Concluído"
        operacao.save()

        # Retornar o JSON com os campos inconsistentes (se houver)
        response_data = {
            'campos_inconsistentes': campos_inconsistentes
        }

        return Response(response_data, status=status.HTTP_201_CREATED)