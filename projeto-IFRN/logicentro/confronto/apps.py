# Importa a classe 'AppConfig', usada para configurar apps no Django.
from django.apps import AppConfig

# Define a classe de configuração do app 'confronto'.
class ConfrontoConfig(AppConfig):

    # Define o tipo padrão de campo de chave primária como 'BigAutoField', que cria IDs automáticos grandes.
    default_auto_field = 'django.db.models.BigAutoField'

    # Define o nome do app como 'confronto', para que o Django saiba como registrá-lo no projeto.
    name = 'confronto'

