from django.shortcuts import render
from .models import PipelineVendas
# Create your views here.
def PipelineView(request):
    pipeline = PipelineVendas.objects.all()

    return render(request, 'pipeline/index.html', {'dados' : pipeline})