from rest_framework import serializers
from confronto.models import Confronto

class ConfrontoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Confronto
        fields = '__all__'