# Importa 'viewsets' (que cria automaticamente as operações CRUD para a API) e 'permissions' (para controle de acesso).
from rest_framework import viewsets, permissions

# Importa o modelo 'Confronto', que representa a tabela do banco de dados.
from confronto.models import Confronto

# Importa o 'ConfrontoSerializer', que converte os dados do modelo 'Confronto' em JSON e vice-versa.
from confronto.serializers import ConfrontoSerializer

# Cria a classe 'ConfrontoViewSet' para definir a API do modelo 'Confronto'.
# Herda de 'ModelViewSet', que automaticamente cria as operações padrão (listar, criar, atualizar, deletar).
class ConfrontoViewSet(viewsets.ModelViewSet):
    
    # Define que a API vai trabalhar com todos os objetos do modelo 'Confronto' do banco de dados.
    queryset = Confronto.objects.all()
    
    # Diz que o 'ConfrontoSerializer' vai ser usado para converter os dados para JSON e vice-versa.
    serializer_class = ConfrontoSerializer
    
    # Define que qualquer pessoa pode acessar essa API (sem restrições de permissão).
    permission_classes = [permissions.AllowAny]