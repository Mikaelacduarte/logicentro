from rest_framework import viewsets, permissions

from motorista.models import Motorista
from motorista.serializers import MotoristaSerializer


# Create your views here.
class MotoristaViewSet(viewsets.ModelViewSet):
    queryset = Motorista.objects.all()
    serializer_class = MotoristaSerializer
    permission_classes = [permissions.AllowAny]