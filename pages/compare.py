import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd

df = pd.read_csv('./datas/avocado.csv', sep=',') 
df.columns = df.columns.str.strip()
regions = sorted(df['region'].unique())

layout = dbc.Container([
    # Bannière bleue pour le titre
    html.Div(
        html.H5("Prix moyen dans le temps", className="text-white m-0 p-2"),
        style={"backgroundColor": "#007bff", "borderRadius": "5px"},
        className="mb-4 mt-3"
    ),
    
    dbc.Row([
        dbc.Col([
            # Badge bleu "Région 1"
            dbc.Badge("Région 1", pill=True, color="info", className="mb-2"),
            dcc.Dropdown(
                id='region-1-dropdown',
                options=[{'label': r, 'value': r} for r in regions],
                value='Albany',  
                clearable=False
            )
        ], xs=12, md=6),
        
        dbc.Col([
            # Badge bleu "Région 2"
            dbc.Badge("Région 2", pill=True, color="info", className="mb-2"),
            dcc.Dropdown(
                id='region-2-dropdown',
                options=[{'label': r, 'value': r} for r in regions],
                value='Atlanta', 
                clearable=False
            )
        ], xs=12, md=6),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col([dcc.Graph(id='graph-region-1')], xs=12, md=6),
        dbc.Col([dcc.Graph(id='graph-region-2')], xs=12, md=6),
    ])
], fluid=True)