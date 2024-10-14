# Define a configuração do app 'motorista', especificando o tipo padrão de campo de chave primária e o nome do app.
from django.apps import AppConfig

class MotoristaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'motorista'

