from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet

# Cria um roteador para definir as URLs da API
router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

# Define as URLs da aplicação
urlpatterns = [
    path('', include(router.urls)),  # Inclui as URLs geradas pelo roteador
    path('api-token-auth/', include('rest_framework.urls')),  # Inclui a URL para autenticação
]