from rest_framework import viewsets, permissions

from confronto.models import Confronto
from confronto.serializers import ConfrontoSerializer

# Create your views here.
class ConfrontoViewSet(viewsets.ModelViewSet):
    queryset = Confronto.objects.all()
    serializer_class = ConfrontoSerializer
    permission_classes = [permissions.AllowAny]