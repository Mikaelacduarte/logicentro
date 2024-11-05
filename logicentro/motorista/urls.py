from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from motorista.views import MotoristaViewSet

router = DefaultRouter()
router.register(r'', MotoristaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.listar_motoristas, name='listar_motoristas'),
]