import dash
import dash_bootstrap_components as dbc
from pages import table, table_cb 

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Le layout appelle celui défini dans pages/table.py (Page 1)
app.layout = table.layout

if __name__ == '__main__':
    app.run(debug=True)  # Utilisez .run_server() si nécessaire