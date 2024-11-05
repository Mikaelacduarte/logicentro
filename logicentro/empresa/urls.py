from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from empresa.views import EmpresaViewSet

router = DefaultRouter()
router.register(r'', EmpresaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', views.listar_empresas, name='listar_empresas'),
]