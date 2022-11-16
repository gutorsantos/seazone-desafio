from django.db import models

# Create your models here.
class Imovel(models.Model):
    id = models.AutoField(primary_key=True)
    hospedes = models.IntegerField(null=False, blank=False)
    banheiros = models.IntegerField(null=False, blank=False)
    pet = models.BooleanField(null=False, blank=False, default=False)
    valor_limpeza = models.DecimalField(null=False, blank=False, max_digits=8, decimal_places=2)
    data_ativacao = models.DateField(null=False, blank=False)
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)