from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from workalendar.america import Brazil
import datetime as dt
from workadays import workdays as wd
import calendar
import numpy as np
import pandas as pd

from .models import Faturamento
from .models import Planejado
from .models import Curso
from .models import Concluido

from .forms import FaturamentoForm
from .forms import PlanejadoForm
from .forms import CursoForm
from .forms import ConcluidoForm
# DATA ATUAL 
today = date.today()
# DIAS TOTAIS DO MÊS
dias_semana =  [ "Seg" , "Ter" , "Qua" , "Qui" , "Sex" , "Sab" , "Dom" ]
monthRange = calendar.monthrange(today.year,10)
dias_totais_mes = int(monthRange[1])
inicio_mes = int(monthRange[0])
mes = np.arange(inicio_mes, dias_totais_mes, 1).tolist()
#df = pd.DataFrame(dias_semana, mes)
# print(mes)
# Create your views here.
def dashboard(request):
    return render(request, 'dashboard/index.html')

def comercial(request):
    faturamentos = Faturamento.objects.all()
    form = FaturamentoForm()
    # tratamento para enviar para o banco
    if request.method == 'POST':
        formOkay = FaturamentoForm(request.POST)
        faturamento = formOkay.save(commit=False)
        # MEIO TEMPO PRA MODIFICAÇÃO

        formOkay.save()
        return redirect('/dashboard/comercial')


    return render(request, 'comercial/index.html', {'faturamentos':faturamentos, 'form': form})
def editarFaturamento(request, id):
    faturamentoEdit = get_object_or_404(Faturamento, pk=id)
    formEdit = FaturamentoForm(instance=faturamentoEdit)

    if(request.method == 'POST'):
        formEdit = FaturamentoForm(request.POST, instance=faturamentoEdit)

        if(formEdit.is_valid()):
            faturamentoEdit.save()
            return redirect('/dashboard/comercial')
        else:
            return render(request, 'comercial/editFaturamento.html', {'formEdit': formEdit, 'faturamentoEdit': faturamentoEdit})
    else:
        return render(request, 'comercial/editFaturamento.html', {'formEdit': formEdit, 'faturamentoEdit': faturamentoEdit})
def deleteFaturamento(request, id):
    faturamento = get_object_or_404(Faturamento, pk=id)
    faturamento.delete()
    return redirect('/dashboard/comercial')



def implantacao(request):
    planejados = Planejado.objects.all()
    cursos = Curso.objects.all()
    concluidos = Concluido.objects.all()

    formPlanejado = PlanejadoForm(self.request.POST or None)
    formCurso = CursoForm(self.request.POST or None)
    formConcluido = ConcluidoForm(self.request.POST or None)
    
    # tratamento para enviar para o banco
    if request.method == 'POST':
        formP = PlanejadoForm(request.POST)
        planejado = formP.save(commit=False)
        # MEIO TEMPO PRA MODIFICAÇÃO
        formP.save()

        # formEC = CursoForm(request.POST)
        # curso = formP.save(commit=False)
        # # MEIO TEMPO PRA MODIFICAÇÃO
        # formEC.save()

        # formC = ConcluidoForm(request.POST)
        # concluido = formC.save(commit=False)
        # # MEIO TEMPO PRA MODIFICAÇÃO
        # formC.save()
               
        return redirect('/dashboard/implantacao')
    return render(request, 'implantacao/index.html', {'planejados':planejados, 'cursos':cursos, 'concluidos':concluidos, 'formConcluido': formConcluido, 'formCurso': formCurso, 'formPlanejado':formPlanejado})