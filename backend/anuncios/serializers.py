from anuncios.models import Anuncio
from rest_framework import serializers
from imoveis.serializers import ImovelSerializer
from rest_framework.permissions import SAFE_METHODS

class AnuncioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Anuncio
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super(AnuncioSerializer, self).__init__(*args, **kwargs)
        request = self.context.get('request')
        if request.method in ['GET']:
            self.Meta.depth = 1
        else:
            self.Meta.depth = 0
        