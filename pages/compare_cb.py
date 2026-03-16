from dash import Output, Input, callback
import plotly.express as px
import pandas as pd

# Chargement et nettoyage
df = pd.read_csv('./datas/avocado.csv', sep=',')
df.columns = df.columns.str.strip()
df['Date'] = pd.to_datetime(df['Date'])

# Pour respecter le Commit 4 : On définit une échelle fixe basée sur 
# les données réelles pour ne pas couper le graphique.
y_min = df['AveragePrice'].min()
y_max = df['AveragePrice'].max()

@callback(
    Output('graph-region-1', 'figure'),
    Input('region-1-dropdown', 'value')
)
def update_graph_1(region):
    # Filtrage par région
    filtered_df = df[df['region'] == region]
    
    # On groupe par date et on fait la moyenne (indispensable pour un trait net)
    df_grouped = filtered_df.groupby('Date')['AveragePrice'].mean().reset_index()
    df_grouped = df_grouped.sort_values(by='Date')
    
    fig = px.line(
        df_grouped, 
        x='Date', 
        y='AveragePrice', 
        title=f"Prix moyen dans le temps - {region}",
        template="plotly_white"
    )
    
    # Respect du sujet : même échelle pour les deux graphiques 
    fig.update_yaxes(range=[y_min, y_max])
    fig.update_traces(line_width=1, line_color="#636EFA") 
    
    return fig

@callback(
    Output('graph-region-2', 'figure'),
    Input('region-2-dropdown', 'value')
)
def update_graph_2(region):
    filtered_df = df[df['region'] == region]
    
    # Même traitement pour la région 2
    df_grouped = filtered_df.groupby('Date')['AveragePrice'].mean().reset_index()
    df_grouped = df_grouped.sort_values(by='Date')
    
    fig = px.line(
        df_grouped, 
        x='Date', 
        y='AveragePrice',
        title=f"Prix moyen dans le temps - {region}",
        template="plotly_white"
    )
    
    # Respect du sujet : même échelle pour les deux graphiques 
    fig.update_yaxes(range=[y_min, y_max])
    fig.update_traces(line_width=1, line_color="#636EFA")
    
    return fig