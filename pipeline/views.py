from django.shortcuts import render
from .models import PipelineVendas
# Create your views here.
def PipelineView(request):
    pipeline = PipelineVendas.objects.all()
    lista = [
        "Cliente",
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
        "OBS",
    ]
    return render(request, 'pipeline/index.html', {'dados' : pipeline, 'lista': lista})