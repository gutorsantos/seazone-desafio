from django.db import models

# Create your models here.
class Reserva(models.Model):
    id = models.AutoField(primary_key=True)
    anuncio_id = models.ForeignKey('anuncios.Anuncio', on_delete=models.CASCADE, null=False, blank=False)
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    total = models.DecimalField(null=False, blank=False, max_digits=8, decimal_places=2)
    comentario = models.TextField(max_length=255, null=False, blank=False)
    hospedes = models.IntegerField(null=False, blank=False)
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)