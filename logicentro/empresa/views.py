from rest_framework import viewsets, permissions

from empresa.models import Empresa
from empresa.serializers import EmpresaSerializer


# Create your views here.
class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [permissions.AllowAny]