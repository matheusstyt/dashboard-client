
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

class Meta_Valor(models.Model):
    updated_at = models.DateField(auto_now_add=True)
    meta =  models.IntegerField()
    def __str__(self):
        return str(self.meta)   
class Licencas_Faltando(models.Model):
    updated_at = models.DateField(auto_now_add=True)
    lincencas_faltando =  models.IntegerField()
    def __str__(self):
        return str(self.lincencas_faltando)   
class Placar_Licensas(models.Model):
    updated_at = models.DateField(auto_now_add=True)
    placar_licensas =  models.IntegerField()
    def __str__(self):
        return str(self.placar_licensas)   

class PipelineA(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    nome_a = models.CharField(max_length=255, null=False)
    uf_a = models.CharField(max_length=255, null=False)
    money_a = models.IntegerField()
    def __str__(self):
        return self.nome
class PipelineB(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    nome_b = models.CharField(max_length=255, null=False)
    uf_b = models.CharField(max_length=255, null=False)
    money_b = models.IntegerField()
    def __str__(self):
        return self.nome
class PipelineC(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    nome_c = models.CharField(max_length=255, null=False)
    uf_c = models.CharField(max_length=255, null=False)
    money_c = models.IntegerField()
    def __str__(self):
        return self.nome
