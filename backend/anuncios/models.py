from django.db import models

# Create your models here.
class Anuncio(models.Model):
    id = models.AutoField(primary_key=True)
    imovel_id = models.ForeignKey('imoveis.Imovel', on_delete=models.CASCADE, null=False, blank=False)
    plataforma = models.CharField(max_length=255, null=False, blank=False)
    taxa = models.DecimalField(null=False, blank=False, max_digits=8, decimal_places=2)
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)