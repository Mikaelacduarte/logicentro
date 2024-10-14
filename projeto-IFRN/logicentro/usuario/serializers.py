from rest_framework import serializers  # Importa o módulo serializers do Django REST Framework, que permite transformar dados complexos em formatos que podem ser facilmente convertidos em JSON ou XML.
from .models import Usuario  # Importa o modelo Usuario do módulo atual, que representa a tabela de usuários no banco de dados.

class UsuarioSerializer(serializers.ModelSerializer):  # Define um serializador para o modelo Usuario, que facilita a conversão de instâncias de Usuario em JSON e vice-versa.
    senha = serializers.CharField(write_only=True)  # Cria um campo 'senha' que será usado apenas para escrita (não será retornado nas respostas).

    class Meta:  # Define a configuração do serializador.
        model = Usuario  # Especifica que este serializador está vinculado ao modelo Usuario.
        fields = ['id_usuario', 'nome', 'email', 'usuario', 'senha']  # Define quais campos do modelo devem ser incluídos na serialização.

    def create(self, validated_data):  # Método chamado para criar um novo usuário com os dados validados.
        senha = validated_data.pop('senha')  # Remove a senha dos dados validados para não ser salva diretamente.
        user = Usuario.objects.create_user(**validated_data, password=senha)  # Cria um novo usuário usando o método create_user, que garante que a senha seja criptografada.
        return user  # Retorna o novo usuário criado.

    def update(self, instance, validated_data):  # Método chamado para atualizar um usuário existente.
        senha = validated_data.pop('senha', None)  # Tenta remover a senha dos dados validados, mas retorna None se não existir.
        if senha:  # Se uma nova senha foi fornecida...
            instance.set_password(senha)  # Atualiza a senha do usuário com a nova senha (criptografando-a).
        instance.save()  # Salva as alterações feitas no usuário.
        return instance  # Retorna a instância do usuário atualizada.
