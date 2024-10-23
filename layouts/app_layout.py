import dash_bootstrap_components as dbc
from dash import html
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import * 
import dash

# App layout
def get_app_layout(page_name, page_top=None, placeholder="Select an option"):
    article_options_label = page_labels[page_name]
    return html.Div(
    style={"display": "flex", "height": "100vh"},
    children=[
        dbc.Col(navbar, width=2, style={"padding": 0}),
        dbc.Col(
            dbc.Container(
                [
                    dbc.Row(dbc.Col(id="page-top-container", children=page_top)),
                    dbc.Row(dbc.Col(id="cards-container", children=[create_plot_card(1, page_name, placeholder=placeholder)]))
                ],
                style={"marginTop": "20px"},
            ),
            width=10,
        ),
    ],
)
