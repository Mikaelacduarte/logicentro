from django.urls import path, include
from rest_framework.routers import DefaultRouter

from empresa.views import EmpresaViewSet

# Cria um roteador para definir as URLs da API
router = DefaultRouter()

# Registra o conjunto de visualizações para as empresas no roteador
router.register(r'empresas', EmpresaViewSet)

# Define as URLs da aplicação
urlpatterns = [
    # Inclui todas as URLs geradas pelo roteador
    path('', include(router.urls)),
]