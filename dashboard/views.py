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

    formPlanejado = PlanejadoForm()
    formCurso = CursoForm()
    formConcluido = ConcluidoForm()
    
    # tratamento para enviar para o banco
    if request.method == 'POST':
        formP = PlanejadoForm(request.POST)
        # planejado = formP.save(commit=False)
        # MEIO TEMPO PRA MODIFICAÇÃO     

        formEC = CursoForm(request.POST)
        # curso = formP.save(commit=False)
        # MEIO TEMPO PRA MODIFICAÇÃO

        formC = ConcluidoForm(request.POST)
        # concluido = formC.save(commit=False)
        # MEIO TEMPO PRA ;MODIFICAÇÃO
        if formP.is_valid():
            formP.save()
        if formEC.is_valid():
            formEC.save()
        if formC.is_valid(): 
            formC.save()   
                
        return redirect('/dashboard/implantacao')
    return render(request, 'implantacao/index.html', {'planejados':planejados, 'cursos':cursos, 'concluidos':concluidos, 'formConcluido': formConcluido, 'formCurso': formCurso, 'formPlanejado':formPlanejado})

def implantacao_planejado_edit(request, id):
    planejado = get_object_or_404(Planejado, pk=id)
    formP = PlanejadoForm(instance=planejado)

    if(request.method == 'POST'):
        formP = PlanejadoForm(request.POST, instance=planejado)
        if(formP.is_valid()):
            formP.save()
            return redirect('/dashboard/implantacao')
        else:
            return render(request, 'implantacao/planejado.html', {'formP': formP})
    else:
        return render(request, 'implantacao/planejado.html', {'formP': formP})

def implantacao_curso_edit(request, id):
    curso = get_object_or_404(Curso, pk=id)
    formC = CursoForm(instance=curso)

    if(request.method == 'POST'):
        formC = CursoForm(request.POST, instance=curso)
        
        if(formC.is_valid()):
            formC.save()
            return redirect('/dashboard/implantacao')
        else:
            return render(request, 'implantacao/curso.html', {'formC': formC})
    else:
        return render(request, 'implantacao/curso.html', {'formC': formC})

def implantacao_concluido_edit(request, id):
    concluido = get_object_or_404(Concluido, pk=id)
    formCO = ConcluidoForm(instance=concluido)

    if(request.method == 'POST'):
        formCO = ConcluidoForm(request.POST, instance=concluido)
        
        if(formCO.is_valid()):
            formCO.save()
            return redirect('/dashboard/implantacao')
        else:
            return render(request, 'implantacao/concluido.html', {'formCO': formCO})
    else:
        return render(request, 'implantacao/concluido.html', {'formCO': formCO})

def implantacao_planejado_delete(request, id):
    planejado = get_object_or_404(Planejado, pk=id)
    planejado.delete()
    return redirect('/dashboard/implantacao') 
def implantacao_curso_delete(request, id):
    curso = get_object_or_404(Curso, pk=id)
    curso.delete()
    return redirect('/dashboard/implantacao') 
def implantacao_concluido_delete(request, id):
    concluido = get_object_or_404(Concluido, pk=id)
    concluido.delete()
    return redirect('/dashboard/implantacao') 