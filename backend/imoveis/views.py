from django.shortcuts import render
from rest_framework import viewsets
from imoveis.models import Imovel
from imoveis.serializers import ImovelSerializer

# Create your views here.

class ImovelViewSet(viewsets.ModelViewSet):
    queryset = Imovel.objects.all() 
    serializer_class = ImovelSerializer