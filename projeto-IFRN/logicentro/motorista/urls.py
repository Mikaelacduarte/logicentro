from django.urls import path, include
from rest_framework.routers import DefaultRouter

from motorista.views import MotoristaViewSet

router = DefaultRouter()
router.register(r'motoristas', MotoristaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]