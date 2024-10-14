# Importa o módulo 'admin' do Django para gerenciar o painel de administração.
from django.contrib import admin

# Importa o modelo 'Motorista' do app 'motorista'.
from motorista.models import Motorista

# Registra o modelo 'Motorista' no painel de administração do Django.
admin.site.register(Motorista)
