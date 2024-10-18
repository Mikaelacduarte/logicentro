from django.urls import path, include
from rest_framework.routers import DefaultRouter

from confronto.views import ConfrontoViewSet

# Criando o roteador para as rotas da API
router = DefaultRouter()
router.register(r'confrontos', ConfrontoViewSet)

# Definindo as URLs para o app
urlpatterns = [
    path('', include(router.urls)),  # Inclui as rotas geradas pelo django rest framework
]