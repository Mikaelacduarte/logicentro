from rest_framework import viewsets, permissions
from django.http import JsonResponse
from veiculo.models import Veiculo
from veiculo.serializers import VeiculoSerializer

# Create your views here.
class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    permission_classes = [permissions.AllowAny]

def procurarVeiculo(request, placa):
    try:
        veiculo=Veiculo.objects.get(placa=placa)
        dados_veiculo={
            'id_veiculo': veiculo.id_veiculo,
            'placa': veiculo.placa,
            'modelo': veiculo.modelo,
            'tipo_veiculo': veiculo.tipo_veiculo
        }

        return JsonResponse(dados_veiculo)
    except Veiculo.DoesNotExist:
        return JsonResponse({'erro': 'Veículo não encontrado'}, status=404)