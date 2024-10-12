from rest_framework import viewsets, permissions

from veiculo.models import Veiculo
from veiculo.serializers import VeiculoSerializer

# Create your views here.
class VeiculoViewSet(viewsets.ModelViewSet):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    permission_classes = [permissions.AllowAny]