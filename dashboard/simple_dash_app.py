import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from django_plotly_dash import DjangoDash
app = DjangoDash('SimpleExample1')


# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


app.layout = html.Div(style={}, children=[


    dcc.Graph(
        id='example-graph-2',
        figure=fig
    )
])

