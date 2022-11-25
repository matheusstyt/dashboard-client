from django.shortcuts import render, get_object_or_404, redirect
from .models import PipelineVendas
import pandas as pd
from .forms import PipelineForm
from datetime import date
import calendar
# Create your views here.
def switch_mes(mes):
    match mes:
        case "January":
            return 1
        case "February":
            return 2
        case "March":
            return 3
        case "April":
            return 4
        case "May":
            return 5
        case "June":
            return 6
        case "July":
            return 7
        case "August":
            return 8
        case "September":
            return 9
        case "October":
            return 10
        case "November":
            return 11
        case "December":
            return 12
        case _:
            print("Uai")
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
    # VALORES PADRÕES QUANDO INICIA A APLICAÇÃO
    mesAtual = 'October'
    anoAtual = today.year
    
    mes = request.GET.get('filter_mes')
    # CONVERTE MES DE NOME PARA NUMERO

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
    pipeline = PipelineVendas.objects.order_by('Cliente').filter(Data_envio_Proposta__month=month).filter(Data_envio_Proposta__year=anoAtual)
    
    # TRATAMENTO DOS PRODUTOS DA TABELA COM OS FILTOS DE MES / ANO
    produtos = PipelineVendas.objects.values_list('Cliente', 'Descricao', 'TotalPrevisto', 'FaturadoMesAtual', 'Data_Faturamento').filter(Data_envio_Proposta__month=month).filter(Data_envio_Proposta__year=anoAtual)
    dfProdutos = pd.DataFrame(produtos)
    dfProdutos.columns = ['Cliente', 'Descricao', 'TotalPrevisto', 'FaturadoMesAtual', 'Data_Faturamento']
    lista_produto = dfProdutos.Descricao.unique()
    data_produtos = pd.DataFrame(columns=['Produto', 'TotalPrevisto', 'FaturadoMesAtual'])
    # LOOP DOS VALORES ÚNICOS DA COLUNA DESCRICAO, CRIA UM DATAFRAME CONTENDO OS PRODUTOS NO LOOP ATUAL E ADICIONA NO DATAFRAME data_produtos
    for produto in lista_produto:
        df = dfProdutos[dfProdutos['Descricao'] == produto]
        data_produtos = data_produtos.append({'Produto' : produto, 'TotalPrevisto': df['TotalPrevisto'].sum(), 'FaturadoMesAtual' : df['FaturadoMesAtual'].sum()}, ignore_index=True)
    print(data_produtos)
    # fim produtos
    
    n_faturados = PipelineVendas.objects.order_by('Cliente').filter(Data_envio_Proposta__isnull=True)
    
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
        "Cliente",
        "UF",
        "Fase",
        "Descrição/Proposta",
        "OMIE",
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
        "Entrega",
        "Pagamento",
        "Contato",
        "Observação",
        "*"
    ]
    context = {
    'dados' : pipeline, 
    'lista': lista, 
    'formPipeline': formPipeline,
    'lista_ano' : lista_ano,
    'lista_mes' : lista_mes,
    'mesAtual' : mesAtual,
    'anoAtual' : anoAtual
    }
    return render(request, 'pipeline/index.html', context)
def pipeline_delete(request, id):
    Pipeline = get_object_or_404(PipelineVendas, pk=id)
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



