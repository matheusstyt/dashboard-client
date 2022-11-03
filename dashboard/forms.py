from django import forms

from .models import Faturamento
class DataInput(forms.DateInput):
    input_type = 'date'

class FaturamentoForm(forms.ModelForm):
    class Meta:
        model = Faturamento
        fields = ('faturamento_dia', 'data_faturamento') 
        widgets ={
            'data_faturamento' : DataInput()
        }