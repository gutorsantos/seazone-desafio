from django.shortcuts import render
from rest_framework import viewsets, mixins
from anuncios.models import Anuncio
from anuncios.serializers import AnuncioSerializer

# Create your views here.

class AnuncioViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Anuncio.objects.all() 
    serializer_class = AnuncioSerializer