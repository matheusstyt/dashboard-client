from django import forms

from .models import Planejado
from .models import Curso
from .models import Concluido
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
class PlanejadoForm(forms.ModelForm):
    class Meta:
        model = Planejado
        fields = ('descricao_planejado', )
class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ('descricao_curso', ) 
class ConcluidoForm(forms.ModelForm):
    class Meta:
        model = Concluido
        fields = ('descricao_concluido', )