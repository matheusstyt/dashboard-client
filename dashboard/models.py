
from django.db import models
 
class Faturamento(models.Model):
    faturamento_dia = models.CharField(max_length=255, null=False)
    data_faturamento = models.DateTimeField(auto_now=False, auto_now_add=False)
    data_update = models.DateField(auto_now=True)

    def __str__(self):
        titulo = f"R$ {float(self.faturamento_dia):.2f}"
        return titulo
    