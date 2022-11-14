from django.shortcuts import render, redirect, get_object_or_404
from datetime import date
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

from .models import PipelineA
from .models import PipelineB
from .models import PipelineC

from . import plotly_app
from .forms import FaturamentoForm
from .forms import PlanejadoForm
from .forms import CursoForm
from .forms import ConcluidoForm
from .forms import MetaForm
from .forms import Placar_LicensasForm
from .forms import Licencas_FaltandoForm
from .forms import PipelineAForm
from .forms import PipelineBForm
from .forms import PipelineCForm
from .graphic import plt
from .graphic import FaturamentoClasse as FaturamentoC
from .graphic import Dataframes
def trial(request):
    return render(request, 'my_first_dash_plotly_app/trial.html')
def dashboard(request):
    planejados = Planejado.objects.all()
    cursos = Curso.objects.all()
    concluidos = Concluido.objects.all()
    pipeLineA = PipelineA.objects.all()
    pipeLineB = PipelineB.objects.all()
    pipeLineC = PipelineC.objects.all()
    faturamento = FaturamentoC()
    context = {
        'pipeline_header' : Dataframes.pipeline_header(), 
        'pipeline_a' : pipeLineA, 
        'pipeline_b' : pipeLineB, 
        'pipeline_c' : pipeLineC, 
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
def pipeline(request):
    pipelineA = PipelineA.objects.all()
    pipelineB = PipelineB.objects.all()
    pipelineC = PipelineC.objects.all()

    formPipelineA = PipelineAForm()
    formPipelineB = PipelineBForm()
    formPipelineC = PipelineCForm()
    
    # tratamento para enviar para o banco
    if request.method == 'POST':
        formPipelineA = PipelineAForm(request.POST)
        # planejado = formP.save(commit=False)
        # MEIO TEMPO PRA MODIFICAÇÃO     

        formPipelineB = PipelineBForm(request.POST)
        # curso = formP.save(commit=False)
        # MEIO TEMPO PRA MODIFICAÇÃO

        formPipelineC = PipelineCForm(request.POST)
        # concluido = formC.save(commit=False)
        # MEIO TEMPO PRA ;MODIFICAÇÃO
        if formPipelineA.is_valid():
            formPipelineA.save()
        if formPipelineB.is_valid():
            formPipelineB.save()
        if formPipelineC.is_valid(): 
            formPipelineC.save()   
                
        return redirect('/dashboard/pipeline')
    return render(request, 'pipeline/index.html', {'pipelineA':pipelineA, 'pipelineB':pipelineB, 'pipelineC':pipelineC, 'formPipelineA': formPipelineA, 'formPipelineB': formPipelineB, 'formPipelineC':formPipelineC})
def pipeline_a_delete(request, id):
    Pipelinea = get_object_or_404(PipelineA, pk=id)
    Pipelinea.delete()
    return redirect('/dashboard/pipeline') 

def pipeline_b_delete(request, id):
    Pipelineb = get_object_or_404(PipelineB, pk=id)
    Pipelineb.delete()
    return redirect('/dashboard/pipeline') 

def pipeline_c_delete(request, id):
    Pipelinec = get_object_or_404(PipelineC, pk=id)
    Pipelinec.delete()
    return redirect('/dashboard/pipeline') 
def pipeline_a_edit(request, id):
    Pipelinea = get_object_or_404(PipelineA, pk=id)
    formPipelineA = PipelineAForm(instance=Pipelinea)

    if(request.method == 'POST'):
        formPipelineA = PipelineAForm(request.POST, instance=Pipelinea)
        
        if(formPipelineA.is_valid()):
            formPipelineA.save()
            return redirect('/dashboard/pipeline')
        else:
            return render(request, 'pipeline/pipelinea.html', {'formPipelineA': formPipelineA})
    else:
        return render(request, 'pipeline/pipelinea.html', {'formPipelineA': formPipelineA})
def pipeline_b_edit(request, id):
    Pipelineb = get_object_or_404(PipelineB, pk=id)
    formPipelineB = PipelineBForm(instance=Pipelineb)

    if(request.method == 'POST'):
        formPipelineB = PipelineBForm(request.POST, instance=Pipelineb)
        
        if(formPipelineB.is_valid()):
            formPipelineB.save()
            return redirect('/dashboard/pipeline')
        else:
            return render(request, 'pipeline/pipelineb.html', {'formPipelineB': formPipelineB})
    else:
        return render(request, 'pipeline/pipelineb.html', {'formPipelineB': formPipelineB})

def pipeline_c_edit(request, id):
    Pipelinec = get_object_or_404(PipelineC, pk=id)
    formPipelineC = PipelineCForm(instance=Pipelinec)

    if(request.method == 'POST'):
        formPipelineC = PipelineAForm(request.POST, instance=Pipelinec)
        
        if(formPipelineC.is_valid()):
            formPipelineC.save()
            return redirect('/dashboard/pipeline')
        else:
            return render(request, 'pipeline/pipelinec.html', {'formPipelineC': formPipelineC})
    else:
        return render(request, 'pipeline/pipelinec.html', {'formPipelineC': formPipelineC})

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
