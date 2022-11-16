from imoveis.models import Imovel
from rest_framework import serializers

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'
        depth = 1
        