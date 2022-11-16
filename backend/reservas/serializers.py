from reservas.models import Reserva
from rest_framework import serializers
from anuncios.serializers import AnuncioSerializer
from imoveis.models import Imovel
from django.utils import timezone

class ReservaSerializer(serializers.ModelSerializer):
    imovel = serializers.SlugRelatedField(many=True, read_only=True, slug_field='name')

    class Meta:
        model = Reserva
        fields = '__all__'
    
    def validate(self, data):
        checkin = data['checkin']
        checkout = data['checkout']

        if checkin > checkout:
            raise serializers.ValidationError("O check-out não pode ocorrer antes do check-in")
        
        ''' ========  Bônus ========
            Mais algumas validações
            i) Tentar fazer reserva para trás da data/hora atual
            ii) Tentar exceder o limite de hospedes permitido

            ========================= ''' 
        if checkin < timezone.now():
            raise serializers.ValidationError("Você não pode fazer uma reserva para o passado")
        
        imovel = Imovel.objects.filter(id=data['anuncio_id'].imovel_id.id)[0]

        if data['hospedes'] > imovel.hospedes:
            raise serializers.ValidationError("Limite máximo de hospedes excedido")
        
        return data