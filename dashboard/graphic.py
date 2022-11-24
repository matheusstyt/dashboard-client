import pandas as pd
import numpy as np
import datetime as dt
import plotly.express as px
import plotly.graph_objs as go
import calendar
from datetime import date
from workalendar.america import Brazil
from workadays import workdays as wd
from dash import Dash, html, dcc
from plotly.offline import plot
from .models import Faturamento
from .models import Meta_Valor
from .models import Placar_Licensas
from .models import Licencas_Faltando
from django.shortcuts import render, redirect, get_object_or_404

def tempoFaturamento(mes, ano):
    # TRATAMENTO DO DATAFRAME
    faturamentos = Faturamento.objects.all().order_by('data_faturamento').filter(data_faturamento__month=mes).filter(data_faturamento__year=ano)
    faturamentos_data = [
        {   'faturamento_dia': i.faturamento_dia,
            'data_faturamento': i.data_faturamento,
        } for i in faturamentos
    ]
    df = pd.DataFrame(faturamentos_data)
    # META
    meta = get_object_or_404(Meta_Valor, pk=2)
    meta = float(meta.meta) 
    # DATA ATUAL 
    today = date.today()
    # DIAS CORRIDOS
    # ULTIMO DIA df['data_faturamento'].iloc[-1]
    # PRIMEIRO DIA df['data_faturamento'].iloc[0]
    try:
        dias_corridos = df[df.columns[0]].count()
        df_faturamento_dia = df['faturamento_dia'].astype('int64')
        # DIAS TOTAIS DO MÊS
        monthRange = calendar.monthrange(today.year,today.month)
        dias_totais_mes = monthRange[1]
        #REAL ACUMULADO
        real_acumulado = df_faturamento_dia.sum()
        # PROJETADO
        x = real_acumulado / dias_corridos
        real_projetado = x * dias_totais_mes
        real_projetado = float("{:.2f}".format(real_projetado)) 
        # PERCENT REAL 
        real_percent = real_acumulado / meta
        real_percent = int(real_percent * 100)
        # PERCENT PROJETADO
        projetado_percent = real_projetado / meta
        projetado_percent = int(projetado_percent * 100)
    except:
        dias_corridos = 0
        meta = 0
        dias_corridos = 0
        dias_totais_mes = 0
        real_acumulado = 0
        real_projetado = 0
        real_percent = 0
        projetado_percent = 0
    return meta, dias_corridos, dias_totais_mes, real_acumulado, real_projetado, real_percent, projetado_percent, grafico_faturamento(df, meta, real_projetado), grafico_meta_projetado(real_percent, projetado_percent)


class plt:
    def suporte():
        lista = [
            ("INJET (1)",21),
            ("INJET > Erro (3)",15),
            ("INJET > Duvida (2)",13),
            ("COLETOR (8)",12),
            ("Solicitação (16)",6),
            ("IDW > Erro (7)",5),
            ("COLETOR > Defeito (9)",4),
            ("IDW (4)",4),
            ("COLETOR > Duvida (10)",3),
            ("ATUALIZAÇÃO (13)",2),
        ]
        npLista = np.array(lista)
        df = pd.DataFrame(npLista, columns=["Categorias", "Chamados"])
        html = df.to_html(index=False)
        return html
    def glpi_suporte():
        nome_ficheiro = 'C:/Users/simone/Documents/desenvolvimento/dashboard/suporte/LISTA DE CLIENTES GLPI.xlsx'
        df = pd.read_excel(nome_ficheiro )
        data = df[['LOCALIAÇÃO', 'Nº DE CHAMADOS COMO REQUERENTE']].loc[df['Nº DE CHAMADOS COMO REQUERENTE'] > 0]
        data.sort_values(by=['Nº DE CHAMADOS COMO REQUERENTE'], ascending=False, inplace=True)
        data.columns = ['Empresa', 'N° de Chamados']
        data['N° de Chamados'] = data['N° de Chamados'].astype('str')
        html = data.to_html(index=False)
        return html

    def grafico_2():
        # TRATAMENTO DO DATAFRAME
        placar_atual = get_object_or_404(Placar_Licensas, pk=1)
        licencas_faltando = get_object_or_404(Licencas_Faltando, pk=1)
        # print('placar_atual.placar_licensas')
        colors = ['#48D2ED', '#488CED', 'darkorange', 'lightgreen']

        fig = go.Figure(data=[go.Pie(labels=['Placar De Licenças','Licenças Faltando'],
                                    values=[placar_atual.placar_licensas,licencas_faltando.lincencas_faltando])])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                        marker=dict(colors=colors, line=dict(color='#283386', width=1,)), title='Distribuição de Licenças')
       
        fig.update_layout( plot_bgcolor = '#212121',
                            font = {'family': 'Arial','size': 12,'color': 'black'},
                           )
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        autosize=True,
        # width=300,
        height=200,
        margin=go.layout.Margin(
            l=0,
            r=0,
            b=2,
            t=0,
            pad = 2
        ))
        gantt_ploty = plot(fig, output_type="div")
        context = {'gantt_ploty': gantt_ploty}
        return gantt_ploty
    
    def grafico_4():
        # TRATAMENTO DO DATAFRAME
        nome_ficheiro = 'C:/Users/simone/Documents/desenvolvimento/dashboard/suporte/chamados-por-status.csv'
        df = pd.read_csv(nome_ficheiro )
        lista = df['Chamados'].values
     
        # FIGURA DE FATURAMENTO
        # gráfico scatter 1
        list_chamados = df['Chamados'].values.tolist()
        layout = go.Layout(
            autosize=True,
            height=400,

            xaxis= go.layout.XAxis(linecolor = 'black',
                                linewidth = 1,
                                mirror = True),

            yaxis= go.layout.YAxis(linecolor = 'black',
                                linewidth = 1,
                                mirror = True),

            margin=go.layout.Margin(
                l=0,
                r=0,
                b=0,
                t=0,
                pad = 4
            )
        )
        fig = go.Figure(data=[go.Pie(labels=['Em atendimento (atribuído)','Solucionado', 'Fechado'], opacity=0.9,
                                    values=list_chamados)], layout=layout)
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                        marker=dict(colors=['#51A2C2', '#3D37B6', '#DA2631'], line=dict(color='#852886', width=1,)), title='Chamados por Categoria')
        fig.update_layout( plot_bgcolor = '#212121', 
                            font = {'family': 'Arial','size': 12,'color': 'black'},
            
                            margin=dict(l=5, r=5, t=5, b=50),)
        fig.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        
        gantt_ploty = plot(fig, output_type="div")
        context = {'gantt_ploty': gantt_ploty}
        return gantt_ploty

def grafico_faturamento(df, meta, real_projetado):
    # CALCULO DE ACUMULADO POR DIA
    percent_dia = []
    line_projetado = []
    acumulado_total = 0
    real_acumulado_por_dia = []
    for item in df['faturamento_dia']:
        acumulado_total = acumulado_total + int(item)
        real_acumulado_por_dia.append(acumulado_total)
        # ADICIONA META NUM ARRAY
        percent_dia.append(meta)
        line_projetado.append(real_projetado)
    # print(percent_dia)
    # CONSTRUÇÃO DO GRÁFICO
    layout = go.Layout(
        autosize=True,
        # width=550,
        height=200,

        xaxis= go.layout.XAxis(linecolor = 'black',
                            linewidth = 1,
                            mirror = True),

        yaxis= go.layout.YAxis(linecolor = 'black',
                            linewidth = 1,
                            mirror = True),

        margin=go.layout.Margin(
            l=0,
            r=0,
            b=0,
            t=10,
            pad = 2
        )
    )
    fig = go.Figure(layout=layout) 
    
    fig.add_trace(go.Line(x = df['data_faturamento'], y = line_projetado,line_color='Green', line_dash='solid', name = 'Projetado'))
    fig.add_trace(go.Line(x = df['data_faturamento'], y = percent_dia,line_color='Red', line_dash='solid', name = 'Meta'))
    fig.add_trace(go.Line(x = df['data_faturamento'], y = real_acumulado_por_dia, line_color='Blue', name = 'Acumulado / dia'))
    fig.add_trace(go.Bar(x = df['data_faturamento'], y = df['faturamento_dia'], name = 'Real / dia', marker_color='rgb(158,202,225)', marker_line_color='rgb(8,48,107)', marker_line_width=1.5, opacity=0.8))
    # fig.add_trace(go.Scatter(x=percent_dia, y=df['faturamento_dia'],
    #             mode='markers',
    #             name='markers'))
    gantt_ploty = plot(fig, output_type="div")
    context = {'gantt_ploty': gantt_ploty}

    return gantt_ploty
def grafico_meta_projetado(real_percent, projetado_percent):
        # FIGURA DE FATURAMENTO
        real_percent = real_percent / 100
        projetado_percent = projetado_percent / 100
        faturamentoL = [
                        ('Realizado', real_percent),
                         ('Projetado', projetado_percent)]
        npLista = np.array(faturamentoL)  
        dfFaturamento = pd.DataFrame(npLista, columns=['Categoria', 'Montante'])    
        
        layout = go.Layout(
            autosize=True,
            # width=265,
             height=200,

            xaxis= go.layout.XAxis(linecolor = 'black',
                                linewidth = 1,
                                mirror = True),

            yaxis= go.layout.YAxis(linecolor = 'black',
                                linewidth = 1,
                                mirror = True),

            margin=go.layout.Margin(
                l=0,
                r=0,
                b=0,
                t=0,
                pad = 2
            )
        )
        fig = go.Figure(layout=layout)
        fig.add_trace(
            go.Histogram(histfunc="sum", 
            y=dfFaturamento['Montante'], 
            x=dfFaturamento['Categoria'], 
            marker_color=['rgb(158,202,225)', '#DD2525'], 
            marker_line_color=['rgb(8,48,107)','#EE0C0C'], 
            marker_line_width=1.5, 
            opacity=0.8,
            name="sum",
            # texttemplate='%{y:.1%f}', 
            textfont_size=20))
        fig.update_layout( plot_bgcolor = 'white',
                            font = {'family': 'Arial','size': 12,'color': 'black'},
                            margin=dict(l=5, r=5, t=15, b=5),             
                            )
        fig.update_traces(texttemplate="%{y:.0%}")
        gantt_ploty = plot(fig, output_type="div")
        context = {'gantt_ploty': gantt_ploty}
        return gantt_ploty