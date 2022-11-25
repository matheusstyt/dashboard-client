from django.db import models

# Create your models here.
class Produtos(models.Model):
    nome = models.CharField(max_length=90)
    faturamento = models.DecimalField(max_digits=8, decimal_places=2)
    quantidade_absoluta = models.IntegerField()
    