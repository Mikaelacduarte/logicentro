# Importa os módulos necessários do Django REST Framework.
from rest_framework import viewsets, permissions

# Importa o modelo 'Empresa' e o serializer correspondente.
from empresa.models import Empresa
from empresa.serializers import EmpresaSerializer

# Define a classe 'EmpresaViewSet', que gerencia as operações de CRUD para o modelo 'Empresa'.
class EmpresaViewSet(viewsets.ModelViewSet):
    # Define a consulta que retorna todos os objetos da tabela 'Empresa'.
    queryset = Empresa.objects.all()

    # Define qual serializer será usado para transformar os dados.
    serializer_class = EmpresaSerializer

    # Permite que qualquer pessoa acesse essas rotas (sem restrições).
    permission_classes = [permissions.AllowAny]
