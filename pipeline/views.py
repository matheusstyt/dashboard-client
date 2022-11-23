from django.shortcuts import render, get_object_or_404, redirect
from .models import PipelineVendas
from .forms import PipelineForm
# Create your views here.

def PipelineView(request):
    
    lista = [
        "*",
        "Cliente",
        "UF",
        "Fase",
        "Descrição/Proposta",
        "OMIE",
        "NF_ Emitidas",
        "Coletor QTDA",
        "Data_ envio Proposta",
        "Revisão + Recente",
        "Data do P.C",
        "Recorrencia",
        "Perpetua",
        "Hardware",
        "Serviços",
        "TOTAL PREVISTO",
        "FATURADO NOVEMBRO",
        "ENTREGA",
        "Pagamento",
        "Contato",
        "Observação",
        "*"
    ]
    lista_mes = (
        'Janeiro',  
        'Fevereiro',
        'Março',
        'Abril',
        'Maio',
        'Junho',
        'Julho',
        'Agosto',
        'Setembro',
         'Outubro',
         'Novembro',
         'Dezembro',
    )
    lista_ano = (
        2017,
        2018,
        2019,
        2020,
        2021,
        2022,
        2023,
        2024,
    )

    mesAtual = 'Outubro'
    anoAtual = 2022
    mes = request.GET.get('filter_mes')
    
    year = request.GET.get('filter_ano')
    year = 2022
    month = 0
    match mes:
        case "Janeiro":
            month = 1
        case "Fevereiro":
            month = 2
        case "Março":
            month = 3
        case "Abril":
            month = 4
        case "Maio":
            month = 5
        case "Junho":
            month = 6
        case "Julho":
            month = 7
        case "Agosto":
            month = 8
        case "Setembro":
            month = 9
        case "Outubro":
            month = 10
        case "Novembro":
            month = 11
        case "Dezembro":
            month = 12
        case _:
            print("Uai")
    mesAtual = request.GET.get('filter_mes')
    anoAtual = request.GET.get('filter_ano')
    if(anoAtual is None):
        anoAtual = 2022
    if(mesAtual is None):
        month = 11
        mesAtual = 'Novembro'
    pipeline = PipelineVendas.objects.order_by('Cliente').filter(Data_envio_Proposta__month=month).filter(Data_envio_Proposta__year__gte=anoAtual)
    formPipeline = PipelineForm()
    # tratamento para enviar para o banco
    print(str(pipeline))
    if request.method == 'POST':
        formPipelineAdd = PipelineForm(request.POST)
        # planejado = formP.save(commit=False)
        if (formPipelineAdd.is_valid()):
            formPipelineAdd.save()
            return redirect('/pipeline')

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



