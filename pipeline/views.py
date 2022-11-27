from django.shortcuts import render, get_object_or_404, redirect
from .models import PipelineVendas
import pandas as pd
from .forms import PipelineForm
from datetime import date
import calendar
# Create your views here.
def switch_mes(mes):
    if mes == "January":
        return 1
    elif mes == "February":
        return 2
    elif mes == "March":
        return 3
    elif mes == "April":
        return 4
    elif mes == "May":
        return 5
    elif mes == "June":
        return 6
    elif mes == "July":
        return 7
    elif mes == "August":
        return 8
    elif mes == "September":
        return 9
    elif mes == "October":
        return 10
    elif mes == "November":
        return 11
    elif mes == "December":
        return 12
def PipelineView(request):
    today = date.today()
    
    # GERANDO LISTA DE MES
    lista_mes = []
    for i in range(1, 13):
        lista_mes.append(calendar.month_name[i])
    # GERAND LSITA DE ANO
    lista_ano = []  
    for i in range(2015, today.year+1):
        lista_ano.append(i)
    # LISTA DE OP
    lista_fatu = ['Sim', 'Não']
    # VALORES PADRÕES QUANDO INICIA A APLICAÇÃO
    mesAtual = 'October'
    anoAtual = today.year
    faturados_option = True
    faturadoAtual = "Sim"
    mes = request.GET.get('filter_mes')
    
    # CONVERTE MES DE NOME PARA NUMERO
    option = request.GET.get('faturados_option')
    if (option is None):
        option = 'Sim'
        faturadoAtual = 'Sim'
    else:
        faturadoAtual = option

    month = switch_mes(mes)

    # RECUPERA DADOS PELA REQUISIÇÃO
    mesAtual = request.GET.get('filter_mes')
    anoAtual = request.GET.get('filter_ano')

    # VERIFICA SE ESTÁ VAZIO NO FRONT END E ATRIBUI O VALOR CASO TRUE
    if(anoAtual is None):
        anoAtual = today.year
    if(mesAtual is None):
        month = today.month
        mesAtual = 'November'
    
    
    dados_pipeline = pd.DataFrame(list(PipelineVendas.objects.all().values().filter(Data_doPC__month=month).filter(Data_doPC__year=anoAtual)))
    try:
        dados_pipeline = dados_pipeline[['id', 'Cliente', 'UF', 'Fase', 'OMIE', 'idProposta', 'Descricao', 'NF_Emitidas', 'Qtd_Coletor','Data_envio_Proposta', 'RevisaoRecente', 
        'Data_doPC', 'Recorrencia', 'Perpetua', 'Hardware', 'Servicos', 'TotalPrevisto', 'FaturadoMesAtual', 'Data_Faturamento', 'Entrega', 'Pagamento', 'Contato', 'OBS']]   
        # TRATANDO A OPÇÃO DE FATURADO
        dados_none = pd.DataFrame(list(PipelineVendas.objects.all().values().filter(Data_doPC__isnull=True)))
        dados_none = dados_none[['id', 'Cliente', 'UF', 'Fase', 'OMIE', 'idProposta', 'Descricao', 'NF_Emitidas', 'Qtd_Coletor','Data_envio_Proposta', 'RevisaoRecente', 
        'Data_doPC', 'Recorrencia', 'Perpetua', 'Hardware', 'Servicos', 'TotalPrevisto', 'FaturadoMesAtual', 'Data_Faturamento', 'Entrega', 'Pagamento', 'Contato', 'OBS']]
        for index, row2 in dados_none.iterrows():
            if row2['Data_doPC'] != None:
                dados_none.drop(dados_none.index[index], inplace=True)
        dados_pipeline = pd.concat([dados_pipeline, dados_none])
        if option == 'Sim':
            option = 'Sim'
            for index1, row3 in dados_pipeline.iterrows():
                if row3['FaturadoMesAtual'] != None:
                    print(index1)
                    dados_pipeline.drop(dados_pipeline.index[index1], inplace=True)
    except:
        dados_pipeline = pd.DataFrame(columns=['id', 'Cliente', 'UF', 'Fase', 'OMIE', 'idProposta', 'Descricao', 'NF_Emitidas', 'Qtd_Coletor','Data_envio_Proposta', 'RevisaoRecente', 
        'Data_doPC', 'Recorrencia', 'Perpetua', 'Hardware', 'Servicos', 'TotalPrevisto', 'FaturadoMesAtual', 'Data_Faturamento', 'Entrega', 'Pagamento', 'Contato', 'OBS'])

    


    n_faturados = PipelineVendas.objects.order_by('Cliente').filter(Data_doPC__isnull=True)
    
    formPipeline = PipelineForm()
    # tratamento para enviar para o banco

    if request.method == 'POST':
        formPipelineAdd = PipelineForm(request.POST)
        # planejado = formP.save(commit=False)
        if (formPipelineAdd.is_valid()):
            formPipelineAdd.save()
            return redirect('/pipeline')
    lista = [
        "*",
        'ID',
        "Cliente",
        "UF",
        "Fase",
        "OMIE",
        "Código da proposta",
        "Descrição/Proposta",
        "NF_ Emitidas",
        "Coletor QTDA",
        "Data de envio da Proposta",
        "Revisão + Recente",
        "Data do P.C",
        "Recorrencia",
        "Perpetua",
        "Hardware",
        "Serviços",
        "Total previsto",
        "Faturado ",
        "Data do Faturamento",
        "Entrega",
        "Pagamento",
        "Contato",
        "Observação",
        "*"
    ]
    op = ['Faturados', 'Não Faturados']

    context = {
    'dados_pipeline' : dados_pipeline   ,
    'lista': lista, 
    'faturadoAtual' : faturadoAtual,
    'lista_fatu' : lista_fatu,
    'formPipeline': formPipeline,
    'lista_ano' : lista_ano,
    'lista_mes' : lista_mes,
    'mesAtual' : mesAtual,
    'anoAtual' : anoAtual,
    'op' : op, 
    'faturados_option' : faturados_option
    }
    return render(request, 'pipeline/index.html', context)
def pipeline_delete(request, id):
    Pipeline = get_object_or_404(PipelineVendas, id=id)
    Pipeline.delete()
    return redirect('/pipeline') 

def pipeline_edit(request, id):
    Pipeline = get_object_or_404(PipelineVendas, pk=id)
    formPipeline = PipelineForm(instance=Pipeline)

    if(request.method == 'POST'):
        formPipeline = PipelineForm(request.POST, instance=Pipeline)
        
        if(formPipeline.is_valid()):
            formPipeline.save()
            return redirect('/pipeline')
        else:
            return render(request, 'edit/index.html', {'formPipeline': formPipeline})
    else:
        return render(request, 'edit/index.html', {'formPipeline': formPipeline})



