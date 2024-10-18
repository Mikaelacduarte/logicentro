from django.urls import include, path
from rest_framework.routers import DefaultRouter

from operacao.views import OperacaoViewSet

router = DefaultRouter()
router.register(r'operacoes', OperacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]