from rest_framework import viewsets, permissions  # Importa as classes necessárias do Django REST Framework.

from veiculo.models import Veiculo  # Importa o modelo Veiculo para usar nas operações.
from veiculo.serializers import VeiculoSerializer  # Importa o serializador VeiculoSerializer para formatar os dados.

# Criação da classe VeiculoViewSet para gerenciar operações do modelo Veiculo.
class VeiculoViewSet(viewsets.ModelViewSet):  # Define uma ViewSet que fornece ações padrão (CRUD) para o modelo.
    queryset = Veiculo.objects.all()  # Define a consulta que retorna todos os veículos.
    serializer_class = VeiculoSerializer  # Define o serializador a ser usado para formatar os dados.
    permission_classes = [permissions.AllowAny]  # Permite acesso a todos, sem necessidade de autenticação.
