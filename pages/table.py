import dash_bootstrap_components as dbc
from dash import dcc, dash_table
import pandas as pd

# Chargement des données
df = pd.read_csv('./datas/avocado.csv', sep=',')  # Change sep if needed
df.columns = df.columns.str.strip()  # Nettoyage des noms de colonnes

regions = sorted(df['region'].unique())
types = ['Tous'] + sorted(df['type'].unique().tolist())

layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        dbc.Label("Sélectionner une région:", className="fw-bold"),
                        dcc.Dropdown(
                            id='region-dropdown',
                            options=[{'label': r, 'value': r} for r in regions],
                            value=regions[0],  # Défaut : première région
                            clearable=False,
                            className="mb-3"
                        )
                    ], xs=12, md=6),  # Responsivité demandée
                    
                    dbc.Col([
                        dbc.Label("Sélectionner un type:", className="fw-bold"),
                        dcc.Dropdown(
                            id='type-dropdown',
                            options=[{'label': t, 'value': t} for t in types],
                            value='Tous',  # Option "Tous"
                            clearable=False,
                            className="mb-3"
                        )
                    ], xs=12, md=6),
                ], className="mb-4"),

                dash_table.DataTable(
                    id='avocado-table',
                    # Exclusion des colonnes spécifiées dans le sujet
                    columns=[
                        {"name": i, "id": i} for i in df.columns 
                        if i not in ["Unnamed: 0", "4046", "4225", "4770", "Small Bags", "Large Bags", "XLarge Bags"]
                    ],
                    page_size=10,
                    style_table={'overflowX': 'auto'},
                    style_header={
                        'backgroundColor': '#007bff',
                        'color': 'white',
                        'fontWeight': 'bold'
                    },
                    style_cell={'textAlign': 'left'},
                    style_data={'whiteSpace': 'normal', 'height': 'auto'}
                )
            ])
        ], className="shadow-sm"))
    ], className="justify-content-center mt-4")
], fluid=True)