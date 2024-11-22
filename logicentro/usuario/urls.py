# usuario/urls.py

from django.urls import path
from .views.auth import LoginView, LogoutView, CreateUserView  # Certifique-se de que a importação está correta

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', CreateUserView.as_view(), name='create_user'),
]
