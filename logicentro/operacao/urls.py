from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views
from operacao.views import OperacaoViewSet

router = DefaultRouter()
router.register(r'', OperacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.listar_operacoes, name='listar_operacoes'),
]