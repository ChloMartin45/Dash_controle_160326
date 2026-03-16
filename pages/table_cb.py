from dash import Output, Input, callback
import pandas as pd

# IMPORTANT : Vérifiez que le séparateur correspond au fichier réel
df = pd.read_csv('./datas/avocado.csv', sep=',')  # Change sep if needed
df.columns = df.columns.str.strip()  # Nettoyage des noms de colonnes

@callback(
    Output('avocado-table', 'data'),
    [Input('region-dropdown', 'value'),
     Input('type-dropdown', 'value')]
)
def update_table(selected_region, selected_type):
    filtered_df = df.copy()

    # Filtrage par région 
    if selected_region:
        filtered_df = filtered_df[filtered_df['region'] == selected_region]
    
    # Filtrage par type (Gestion de l'option "Tous")
    if selected_type and selected_type != 'Tous':
        filtered_df = filtered_df[filtered_df['type'] == selected_type]

    # Retourne les données filtrées
    return filtered_df.to_dict('records')