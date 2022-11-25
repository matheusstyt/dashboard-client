
from django import forms
from django.forms.widgets import NumberInput
from .models import PipelineVendas
from django.forms.fields import DateField
class PipelineForm(forms.ModelForm):
    Data_envio_Proposta = forms.DateTimeField(label="Data envio da Proposta", required=False, widget=NumberInput(attrs={'type':'date'}))
    Data_doPC = forms.DateTimeField(label="Data do P.C", required=False, widget=NumberInput(attrs={'type':'date'}))
    class Meta: 
        model = PipelineVendas
        fields = (
            'Cliente', 
            'UF', 
            'Fase',
            'idProposta',
            'Descricao', 
            'OMIE', 
            'NF_Emitidas',
            'Qtd_Coletor', 
            'Data_envio_Proposta', 
            'RevisaoRecente',
            'Data_doPC', 
            'Recorrencia', 
            'Perpetua',
            'Hardware', 
            'Servicos', 
            'TotalPrevisto',
            'FaturadoMesAtual', 
            'Data_Faturamento',
            'Entrega', 
            'Pagamento',
            'Contato', 
            'OBS'            
            )

