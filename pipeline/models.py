from django.db import models

# Create your models here.
class PipelineVendas(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    Cliente = models.CharField(max_length=255, blank=False, null=False)
    OP1 = (
        ('RO', 'Rondônia'),
        ('AC', 'Acre'),
        ('AM', 'Amazonas'),
        ('RR', 'Roraima'),
        ('PA', 'Pará'),
        ('AP', 'Amapá'),
        ('TO', 'Tocantins'),
        ('MA', 'Maranhão'),
        ('PI', 'Piauí'),    
        ('CE', 'Ceará'),
        ('RN', 'Rio Grande do Norte'),
        ('PB', 'Paraíba'),
        ('PE', 'Pernambuco'),
        ('AL', 'Alagoas'),
        ('SE', 'Sergipe'),
        ('BA', 'Bahia'),
        ('MG', 'Minas Gerais'),
        ('ES', 'Espírito Santo'),
        ('RJ', 'Rio de Janeiro'),
        ('SP', 'São Paulo'),
        ('PR', 'Paraná'),
        ('SC', 'Santa Catarina'),
        ('RS', 'Rio Grande do Sul'),    
        ('MS', 'Mato Grosso do Sul'),
        ('MT', 'Mato Grosso'),
        ('GO', 'Goiás'),
        ('DF', 'Distrito Federal'),
 
    )
    UF = models.CharField(choices=OP1, max_length=30, blank=True, null=True)
    OP2 = (
        ('Inicio', 'Inicio'),
        ('Negociação', 'Negociação'),
        ('Compras', 'Compras'),
        ('Aprovado', 'Aprovado'),
        
    )
    Fase = models.CharField(choices=OP2, max_length=10, blank=False, null=False)
    Descricao = models.CharField(max_length=100, blank=True, null=True) 
    OMIE = models.CharField(max_length=100, blank=True, null=True)  
    NF_Emitidas = models.CharField(max_length=100, blank=True, null=True)  
    Qtd_Coletor = models.IntegerField(blank=True, null=True) 
    Data_envio_Proposta = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    RevisaoRecente = models.CharField(max_length=50, blank=True, null=True)
    Data_doPC = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    Recorrencia = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    Perpetua = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    Hardware = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    Servicos = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    TotalPrevisto = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    FaturadoMesAtual = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    OP3 = (
        ('Realizada', 'Realizada'),
        ('Pendente', 'Pendente'),
        ('N/A', 'N/A'),
    )
    Entrega = models.CharField(choices=OP3, max_length=50, blank=False, null=False)
    Pagamento = models.CharField(max_length=50, blank=True, null=True)
    Contato = models.CharField(max_length=50, blank=True, null=True)
    OBS = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.Cliente