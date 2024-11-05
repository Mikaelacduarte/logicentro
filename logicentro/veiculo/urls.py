from django.urls import path, include
from rest_framework.routers import DefaultRouter
from veiculo.views import VeiculoViewSet
from .views import procurarVeiculo
from . import views

# Criando o roteador para as rotas da API
router = DefaultRouter()
router.register(r'', VeiculoViewSet)

# Definindo as URLs para o app
urlpatterns = [
    path('', include(router.urls)),  # Inclui as rotas geradas pelo django rest framework
    path('<str:placa>', views.procurarVeiculo, name='procurarVeiculo'),
]