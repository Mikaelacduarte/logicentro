from rest_framework import viewsets, permissions

from operacao.models import Operacao
from operacao.serializers import OperacaoSerializer

# Create your views here.
class OperacaoViewSet(viewsets.ModelViewSet):
    queryset = Operacao.objects.all()
    serializer_class = OperacaoSerializer
    permission_classes = [permissions.AllowAny]