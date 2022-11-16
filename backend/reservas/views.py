from rest_framework import viewsets, mixins
from reservas.models import Reserva
from reservas.serializers import ReservaSerializer

# Create your views here.

class ReservaViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Reserva.objects.all() 
    serializer_class = ReservaSerializer
