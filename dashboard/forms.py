from django import forms

from .models import Planejado
from .models import Curso
from .models import Concluido
from .models import Faturamento
from .models import Meta_Valor
from .models import Licencas_Faltando
from .models import Placar_Licensas
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
class MetaForm(forms.ModelForm):
    class Meta:
        model = Meta_Valor
        fields = ('meta',)
class Placar_LicensasForm(forms.ModelForm):
    class Meta:
        model = Placar_Licensas
        fields = ('placar_licensas',)
class Licencas_FaltandoForm(forms.ModelForm):
    class Meta:
        model = Licencas_Faltando
        fields = ('lincencas_faltando',)







