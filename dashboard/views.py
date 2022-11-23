from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
from django.db.models import Sum

from pipeline.models import PipelineVendas

from workalendar.america import Brazil
import datetime as dt
from workadays import workdays as wd
import calendar
import numpy as np
import pandas as pd
import plotly.express as px
from plotly.offline import plot

from .models import Faturamento
from .models import Planejado
from .models import Curso
from .models import Concluido
from .models import Meta_Valor
from .models import Placar_Licensas
from .models import Licencas_Faltando

from . import plotly_app
from .forms import FaturamentoForm
from .forms import PlanejadoForm
from .forms import CursoForm
from .forms import ConcluidoForm
from .forms import MetaForm
from .forms import Placar_LicensasForm
from .forms import Licencas_FaltandoForm

from .graphic import plt
from .graphic import FaturamentoClasse as FaturamentoC
from .graphic import Dataframes
def trial(request):
    return render(request, 'my_first_dash_plotly_app/trial.html')
def dashboard(request):
    # PIPELINE DADOS 

    pipeline_header = ['Cliente', 'Fase', 'Recorrencia' , 'Perpetua', 'Hardware', 'Serviços']
    pipeline = PipelineVendas.objects.all()

    total_a = 0
    count_a = 0

    total_b = 0
    count_b = 0

    total_c = 0
    count_c = 0

    total_d = 0
    count_d = 0

    for x in pipeline:
        if x.Fase == 'Inicio':
            total_a += x.TotalPrevisto
            count_a += 1
        if x.Fase == 'Negociação':
            total_b += x.TotalPrevisto
            count_b += 1
        if x.Fase == 'Compras':
            total_c += x.TotalPrevisto
            count_c += 1
        if x.Fase == 'Aprovado':
            total_d += x.TotalPrevisto
            count_d += 1

    planejados = Planejado.objects.all()
    cursos = Curso.objects.all()
    concluidos = Concluido.objects.all()
    faturamento = FaturamentoC()
    context = {
        'pipeline_header' : pipeline_header, 
        'pipeline' : pipeline, 
        'total_a' : total_a, 
        'total_b' : total_b, 
        'total_c' : total_c, 
        'total_d' : total_d, 
        'count_a' : count_a, 
        'count_b' : count_b, 
        'count_c' : count_c, 
        'count_d' : count_d, 
        'meta' : faturamento.metaStr,
        'real_projetado' : faturamento.real_projetado,
        'real_acumulado' : faturamento.real_acumulado,
        'real_percent' : faturamento.real_percent,
        'projetado_percent' : faturamento.projetado_percent,
        'planejados': planejados, 
        'cursos' : cursos, 
        'concluidos' : concluidos, 
        'fig1' : plt.grafico_1(), 
        'fig2': plt.grafico_2(), 
        'fig3' : plt.grafico_3(), 
        'fig4' : plt.grafico_4(), 
        'df1': plt.glpi_suporte(), 
        'df2': plt.suporte()}
   
    return render(request, 'dashboard/index.html', context)
def comercial(request):
    faturamentos = Faturamento.objects.all().order_by('-data_faturamento')
    form = FaturamentoForm()
    # editar meta
    meta = get_object_or_404(Meta_Valor, pk=2)
    lincencas_faltando = get_object_or_404(Licencas_Faltando, pk=1)
    placar_licensas = get_object_or_404(Placar_Licensas, pk=1)

    formMeta = MetaForm(instance=meta)
    formLicensas = Licencas_FaltandoForm(instance=lincencas_faltando)
    formPlacar = Placar_LicensasForm(instance=placar_licensas)

    # tratamento para enviar para o banco
    if request.method == 'POST':
        # SALVAMENTO DO FORMULÁRIO FATURAMENTO ADIÇÃO
        formOkay = FaturamentoForm(request.POST)
        if(formOkay.is_valid()):
            formOkay.save()
            return redirect('/dashboard/comercial')
            
        # SALVAMENTO DO FORMULÁRIO META EDITAR
        formMeta = MetaForm(request.POST, instance=meta)
        if(formMeta.is_valid()):
            formMeta.save()
            return redirect('/dashboard/comercial')
        
        # SALVAMENTO DO FORMULÁRIO LICENSAS EDITAR
        formLicensas = Licencas_FaltandoForm(request.POST, instance=lincencas_faltando)
        if(formLicensas.is_valid()):
            formLicensas.save()
            return redirect('/dashboard/comercial')

        # SALVAMENTO DO FORMULÁRIO PLACAR EDITAR
        formPlacar = Placar_LicensasForm(request.POST, instance=placar_licensas)
        if(formPlacar.is_valid()):
            formPlacar.save()
            return redirect('/dashboard/comercial')


    return render(request, 'comercial/index.html', {'faturamentos':faturamentos, 'form': form, 'formMeta':formMeta, 'formLicensas': formLicensas, 'formPlacar': formPlacar})

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
def editarMeta(request, id):
    meta = get_object_or_404(Meta_Valor, pk=2)
    formMeta = MetaForm(instance=meta)

    if(request.method == 'POST'):
        formMeta = MetaForm(request.POST, instance=meta)
        
        if(formMeta.is_valid()):
            formMeta.save()
            return redirect('/dashboard/implantacao')
        else:
            return render(request, 'implantacao/concluido.html', {'formCO': formCO})
    else:
        return render(request, 'implantacao/concluido.html', {'formCO': formCO})
