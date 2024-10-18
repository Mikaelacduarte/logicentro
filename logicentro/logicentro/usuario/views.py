from django.db import transaction  # Garante que operações no banco de dados sejam tratadas como uma única unidade

from rest_framework import (  # Importa funcionalidades do framework Django REST para criar APIs
    viewsets, permissions, status, Response
)

from rest_framework.authtoken.models import Token  # Modelo para tokens de autenticação

from .models import Usuario  # Importa o modelo de Usuário (provavelmente armazena dados como nome, email, etc.)
from .serializers import UsuarioSerializer  # Importa o serializador para o modelo Usuário (define como os dados serão formatados)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()  # Permite acesso a todos os objetos do modelo Usuário
    serializer_class = UsuarioSerializer  # Define o serializador a ser usado para formatar os dados

    permission_classes = [permissions.AllowAny]  # Permite que qualquer um crie um novo usuário

    def create(self, request, *args, **kwargs):
        # Cria um novo usuário utilizando o método padrão de criação
        response = super().create(request, *args, **kwargs)

        # Obtém o usuário recém-criado com base no email
        user = Usuario.objects.get(email=response.data['email'])

        # Cria ou recupera um token de autenticação para o usuário
        token, created = Token.objects.get_or_create(user=user)

        # Retorna uma resposta com o token e o email do usuário
        return Response({'token': token.key, 'email': user.email})

    def update(self, request, *args, **kwargs):
        # Permite apenas usuários autenticados atualizarem suas informações
        self.permission_classes = [permissions.IsAuthenticated]

        # Atualiza as informações do usuário utilizando o método padrão de atualização
        return super().update(request, *args, **kwargs)