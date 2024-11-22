# usuario/views/auth.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import status

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user and user.is_active:
            # Gera os tokens para o usuário
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': {
                    'email': user.email,
                    'nome': user.nome,
                    'cargo': user.cargo,
                }
            }, status=status.HTTP_200_OK)
        return Response({'detail': 'Credenciais inválidas ou conta inativa.'}, status=status.HTTP_401_UNAUTHORIZED)

# usuario/views/auth.py

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Obtém o token de refresh e o adiciona à blacklist
            token = RefreshToken(request.data.get('refresh'))
            token.blacklist()  # Isso exige que o blacklist esteja habilitado
            return Response({'detail': 'Logout realizado com sucesso.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'detail': 'Erro ao realizar logout.'}, status=status.HTTP_400_BAD_REQUEST)


class CreateUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        nome = request.data.get('nome')
        cargo = request.data.get('cargo')

        # Verifique se o usuário já existe
        if User.objects.filter(email=email).exists():
            return Response({'detail': 'Usuário já existe'}, status=status.HTTP_400_BAD_REQUEST)

        # Crie um novo usuário
        user = User.objects.create(
            email=email,
            password=make_password(password),  # Importante: hash a senha!
            first_name=nome,
            last_name=cargo
        )

        return Response({
            'detail': 'Usuário criado com sucesso',
            'user': {
                'email': user.email,
                'nome': user.first_name,
                'cargo': user.last_name,
            }
        }, status=status.HTTP_201_CREATED)