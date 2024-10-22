import dash_bootstrap_components as dbc
from dash import html
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import * 

# App layout
def get_app_layout():
    return html.Div(
    style={"display": "flex", "height": "100vh"},
    children=[
        dbc.Col(navbar, width=2, style={"padding": 0}),
        dbc.Col(
            dbc.Container(
                [
                    dbc.Row(dbc.Col(id="cards-container", children=[create_card(1)])),
                    dbc.Row(
                        dbc.Col(
                            html.Div(
                                [
                                    html.I(className="fas fa-plus", style={"fontSize": "30px", "cursor": "pointer"}),
                                    dbc.Tooltip("Add Plot", target="add-card-icon", placement="top"),
                                ],
                                id="add-card-icon",
                                style={"textAlign": "center", "marginTop": "20px"},
                            )
                        )
                    ),
                ],
                style={"marginTop": "20px"},
            ),
            width=10,
        ),
    ],
)
