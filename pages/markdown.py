import dash_bootstrap_components as dbc
from dash import html, dcc
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def read_markdown_file(file_name):
    file_path = os.path.join(BASE_DIR, 'assets', file_name)
    
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    return f"Fichier {file_name} non trouvé à l'emplacement : {file_path}"

content1 = read_markdown_file('expli1.md')
content2 = read_markdown_file('expli2.md')
content3 = read_markdown_file('expli3.md')

layout = dbc.Container([
    html.Div(
        html.H2("PRÉSENTATION DE DASH", className="text-white m-0 p-4 text-center"),
        style={
            "backgroundImage": "url('/assets/dash.jpg')", 
            "backgroundSize": "cover",
            "backgroundPosition": "center",
            "borderRadius": "5px",
            "height": "150px",
            "display": "flex",
            "alignItems": "center",
            "justifyContent": "center"
        },
        className="mb-4 mt-3"
    ),

    dbc.Accordion([
        dbc.AccordionItem(
            dcc.Markdown(content1),
            title="Accueil",
        ),
        dbc.AccordionItem(
            dcc.Markdown(content2),
            title="Layout",
        ),
        dbc.AccordionItem(
            dcc.Markdown(content3),
            title="CallBack",
        ),
    ], start_collapsed=True)
], fluid=True)