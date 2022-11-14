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

class FaturamentoClasse(): 
    meta = 0
    metaStr = ''
    real_acumulado = 0
    real_projetado = 0
    dias_corridos = 0
    dias_totais_mes = 0
    real_percent = 0
    projetado_percent = 0 
    def __init__(self, *args, **kwargs):
        super(CLASS_NAME, self).__init__(*args, **kwargs)
    
    def __init__(self):
        #DATA FRAME
        df = df_faturamento()
        # META
        meta = get_object_or_404(Meta_Valor, pk=2)
        meta = int(meta.meta)
        # DATA ATUAL 
        today = date.today()
        # DIAS CORRIDOS
        # ULTIMO DIA df['data_faturamento'].iloc[-1]
        # PRIMEIRO DIA df['data_faturamento'].iloc[0]
        dias_corridos = df[df.columns[0]].count()
        df = df['faturamento_dia'].astype('int64')
        # DIAS TOTAIS DO MÊS
        monthRange = calendar.monthrange(today.year,today.month)
        dias_totais_mes = monthRange[1]
        #REAL ACUMULADO
        real_acumulado = df.sum()
        # PROJETADO
        x = real_acumulado / dias_corridos
        real_projetado = x * dias_totais_mes
        # PERCENT REAL 
        real_percent = real_acumulado / meta
        # PERCENT PROJETADO
        projetado_percent = real_projetado / meta

        self.meta = float("{:.2f}".format(meta))
        self.metaStr = float("{:.2f}".format(meta))
        self.real_acumulado = float("{:.2f}".format(real_acumulado))
        self.real_projetado = float("{:.2f}".format(real_projetado)) 
        self.dias_corridos = dias_corridos
        self.dias_totais_mes = dias_totais_mes
        self.real_percent = int(real_percent * 100)
        self.projetado_percent = int(projetado_percent * 100)

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
    def grafico_1():
        faturamento = FaturamentoClasse()
        df = df_faturamento()
        # CALCULO DE ACUMULADO POR DIA
        acumulado_total = 0
        real_acumulado_por_dia = []
        for item in df['faturamento_dia']:
            acumulado_total = acumulado_total + int(item)
            real_acumulado_por_dia.append(acumulado_total)
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
                t=0,
                pad = 2
            )
        )
        fig = go.Figure(layout=layout) 
        fig.add_hline(y=faturamento.meta, opacity=1, line_width=2, line_dash='dash', line_color='Red', name='Meta')
        fig.add_trace(go.Line(x = df['data_faturamento'], y = real_acumulado_por_dia, name = 'Acumulado / dia'))
        fig.add_trace(go.Bar(x = df['data_faturamento'], y = df['faturamento_dia'], name = 'Real / dia'))
        gantt_ploty = plot(fig, output_type="div")
        context = {'gantt_ploty': gantt_ploty}

        return gantt_ploty

    def grafico_2():
        # TRATAMENTO DO DATAFRAME
        placar_atual = get_object_or_404(Placar_Licensas, pk=1)
        licencas_faltando = get_object_or_404(Licencas_Faltando, pk=1)
        print('placar_atual.placar_licensas')
        colors = ['#48D2ED', '#488CED', 'darkorange', 'lightgreen']

        fig = go.Figure(data=[go.Pie(labels=['Placar De Licenças','Licenças Faltando'],
                                    values=[placar_atual.placar_licensas,licencas_faltando.lincencas_faltando])])
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                        marker=dict(colors=colors, line=dict(color='#000000', width=1,)), title='Distribuição de Licenças')
       
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
    def grafico_3():
        # TRATAMENTO DO DATAFRAME
        faturamento = FaturamentoClasse()
        # FIGURA DE FATURAMENTO
        faturamentoL = [('Meta', faturamento.meta),
                        ('Realizado', faturamento.real_acumulado),
                        ('Projetado', faturamento.real_projetado)]
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
        color_d = ["#DD2525", "#3675D6 ", "#4B4FD6"]

        fig.add_trace(
            go.Histogram(histfunc="sum", 
            y=dfFaturamento['Montante'], 
            x=dfFaturamento['Categoria'], 
            marker={'color': color_d},
            name="sum",texttemplate="%{y}", 
            textfont_size=20))
        fig.update_layout( plot_bgcolor = 'white',
                            font = {'family': 'Arial','size': 12,'color': 'black'},
                            margin=dict(l=5, r=5, t=15, b=5),
                            
                            )
        gantt_ploty = plot(fig, output_type="div")
        context = {'gantt_ploty': gantt_ploty}
        return gantt_ploty
    def grafico_4():
        # TRATAMENTO DO DATAFRAME
        nome_ficheiro = 'C:/Users/simone/Documents/desenvolvimento/dashboard/suporte/chamados-por-status.csv'
        df = pd.read_csv(nome_ficheiro )
        lista = df['Chamados'].values
        faturamento = FaturamentoClasse()
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
        fig = go.Figure(data=[go.Pie(labels=['Em atendimento (atribuído)','Solucionado', 'Fechado'],
                                    values=list_chamados)], layout=layout)
        fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                        marker=dict(colors=['#F5894F', '#3D37B6', '#DA2631'], line=dict(color='#000000', width=1,)), title='Chamados por Categoria')
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
def df_faturamento():
    # TRATAMENTO DO DATAFRAME
    faturamentos = Faturamento.objects.all()
    
    faturamentos_data = [
        {
            'faturamento_dia': i.faturamento_dia,
            'data_faturamento': i.data_faturamento,

        } for i in faturamentos
    ]
    df = pd.DataFrame(faturamentos_data)
    df['data_faturamento'] = pd.to_datetime(df['data_faturamento'], dayfirst=True)
    df.sort_values(["data_faturamento"], axis=0,ascending=True, inplace=True)

    return df
class Dataframes:
    def pipeline_header():
        lista = [
            ("Cliente A", 70000, 'Amazonas'), 
            ("Cliente B", 65000, 'Bahia'), 
            ("Cliente C", 15000, 'Amazonas'), 
            ("Cliente D", 70060, 'Bahia'),
            ("Cliente E", 23000, 'Amazonas'),
        ]
        npLista = np.array(lista)
        df = pd.DataFrame(npLista, columns=['Clientes', '$$$', 'UF'])
        return df
    def pipeline_a():
        lista = [
            ("Cliente A", 70000, 'Amazonas'), 
            ("Cliente B", 65000, 'Bahia'), 
            ("Cliente C", 15000, 'Amazonas'), 
            ("Cliente D", 70060, 'Bahia'),
            ("Cliente E", 23000, 'Amazonas'),
        ]
        npLista = np.array(lista)
        df = pd.DataFrame(npLista, columns=['Clientes', '$$$', 'UF'])
        html = df.to_html(index=False, header=False)
        return html
    def pipeline_b():
        lista = [
            ("Cliente F", 54000, 'Amazonas'), 
            ("Cliente G", 60000, 'Amazonas'), 
            ("Cliente H", 19000, 'São Paulo'), 
            ("Cliente I", 50000, 'São Paulo'),
            ("Cliente J", 23000, 'Amazonas'),
        ]
        npLista = np.array(lista)
        df = pd.DataFrame(npLista, columns=['Clientes', '$$$', 'UF'])
        html = df.to_html(index=False, header=False)
        return html
    def pipeline_c():
        lista = [
            ("Cliente K", 44000, 'Amazonas'), 
            ("Cliente L", 56000, 'Bahia')
            # ("Cliente M", 15000, 'São Paulo'), 
            # ("Cliente N", 12000, 'Bahia'),
            # ("Cliente O", 23000, 'Amazonas'),
        ]
        npLista = np.array(lista)
        df = pd.DataFrame(npLista, columns=['Clientes', '$$$', 'UF'])
        html = df.to_html(index=False, header=False)
        return html
