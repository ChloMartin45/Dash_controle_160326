import dash
import dash_bootstrap_components as dbc
from dash import dcc, html, Input, Output

# Import des layouts et des callbacks (crucial pour enregistrer les interactions)
from pages import table, table_cb
from pages import compare, compare_cb

# Initialisation de l'app (on retire use_pages=True pour garder le contrôle manuel)
app = dash.Dash(
    __name__, 
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True # Recommandé pour les applis multipages
)

# Layout principal
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    
    dbc.NavbarSimple(
        children=[
            # Utilisation de dcc.Link pour éviter de recharger toute la page
            dbc.NavItem(dcc.Link("Données", href="/", className="nav-link")),
            dbc.NavItem(dcc.Link("Comparaison", href="/compare", className="nav-link")),
        ],
        brand="🥑 Avocado Dashboard",
        color="primary",
        dark=True,
        className="mb-4"
    ),
    
    # Conteneur où le contenu des pages sera injecté
    dbc.Container(id='page-content', fluid=True)
])

# Callback pour le routage (Gestion du changement de page)
@app.callback(
    Output('page-content', 'children'),
    [Input('url', 'pathname')]
)
def display_page(pathname):
    if pathname == '/compare':
        return compare.layout
    else:
        return table.layout # Page par défaut (/)

if __name__ == '__main__':
    app.run(debug=True)