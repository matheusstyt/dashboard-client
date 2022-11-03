from django.shortcuts import render, redirect
from datetime import date
from workalendar.america import Brazil
import datetime as dt
from workadays import workdays as wd
import calendar
import numpy as np
import pandas as pd
from .models import Faturamento
from .forms import FaturamentoForm
# DATA ATUAL 
today = date.today()
# DIAS TOTAIS DO MÊS
dias_semana =  [ "Seg" , "Ter" , "Qua" , "Qui" , "Sex" , "Sab" , "Dom" ]
monthRange = calendar.monthrange(today.year,10)
dias_totais_mes = int(monthRange[1])
inicio_mes = int(monthRange[0])
mes = np.arange(inicio_mes, dias_totais_mes, 1).tolist()
#df = pd.DataFrame(dias_semana, mes)
print(mes)
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
def novoFaturamento(request):
    form = FaturamentoForm()
    return render(request, 'comercial/novoFaturamento.html', {'form': form})