from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True)

    class Meta:
        model = Usuario
        fields = ['id_usuario', 'nome', 'email', 'usuario', 'senha']

    def create(self, validated_data):
        senha = validated_data.pop('senha')
        user = Usuario.objects.create_user(**validated_data, password=senha)
        return user

    def update(self, instance, validated_data):
        senha = validated_data.pop('senha', None)
        if senha:
            instance.set_password(senha)
        instance.save()
        return instance