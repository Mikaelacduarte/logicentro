from django.db import transaction
from rest_framework import viewsets, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]  # Permitir criação de usuário (POST) sem autenticação

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        user = Usuario.objects.get(email=response.data['email'])
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'email': user.email})

    def update(self, request, *args, **kwargs):
        # Permitir update apenas para usuários autenticados
        self.permission_classes = [permissions.IsAuthenticated]
        return super().update(request, *args, **kwargs)