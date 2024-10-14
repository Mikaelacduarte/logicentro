# Importa o módulo 'serializers' do Django REST Framework. Este módulo permite converter dados entre formatos como JSON e objetos do Django (modelos).
from rest_framework import serializers

# Importa o modelo 'Confronto' da aplicação 'confronto'. Este é o modelo que vamos converter para JSON e vice-versa.
from confronto.models import Confronto

 # Cria a classe 'ConfrontoSerializer', que vai converter dados do modelo 'Confronto' para JSON e de volta para objetos do modelo.
    # Herda de 'serializers.ModelSerializer', que já traz métodos prontos para fazer essa conversão automaticamente.
class ConfrontoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Confronto
         # Aqui estamos dizendo que o 'serializer' está ligado ao modelo 'Confronto'. Ele usará este modelo como base.
        fields = '__all__'
        # O campo 'fields' define quais campos do modelo serão incluídos na conversão.
        # Usando '__all__', indicamos que todos os campos do modelo 'Confronto' devem ser incluídos no JSON.