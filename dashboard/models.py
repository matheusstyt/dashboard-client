
from django.db import models
 
class Faturamento(models.Model):
    faturamento_dia = models.CharField(max_length=255, null=False)
    data_faturamento = models.DateTimeField(auto_now=False, auto_now_add=False)
    data_update = models.DateField(auto_now=True)

    def __str__(self):
        titulo = f"R$ {float(self.faturamento_dia):.2f}"
        return titulo
class Planejado(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    descricao_planejado = models.TextField()
    def __str__(self):
        return self.descricao_planejado
    
class Curso(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    descricao_curso = models.TextField()
    def __str__(self):
        return self.descricao_curso
class Concluido(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    descricao_concluido = models.TextField()
    def __str__(self):
        return self.descricao_concluido   