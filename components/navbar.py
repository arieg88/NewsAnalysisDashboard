import dash_bootstrap_components as dbc
from dash import html
from configurations.config import *

navbar = dbc.Navbar(
    dbc.Nav(
        [
            dbc.NavLink(
                html.Img(src=project_logo, style={"width": "100%", "maxHeight": "10vh", "marginTop": "10px"}),
                active="exact",
                style={"backgroundColor": "transparent", "border": "none"}
            ),
            html.Br(),
            dbc.Stack(
                dbc.NavLink(
                    html.Img(src=home_icon, style={"width": "50%", "maxHeight": "10vh"}),
                    href="/",
                    active="exact",
                    style={"backgroundColor": "transparent", "border": "none"}
                ),
            ),
            dbc.NavLink(
                html.Img(src=user_icon, style={"width": "100%", "maxHeight": "10vh", "marginBottom": "10px"}),
                href="/aboutme",
                active="exact",
                style={"backgroundColor": "transparent", "border": "none"}
            ),
        ],
        # vertical="md",
        style={
            "textAlign": "center",
            "display": "flex",
            "flexDirection": "column",
            "height": "100%",
            "justifyContent": "space-between",
        },
    ),
    color="dark",
    dark=True,
    style={
        "height": "100vh",
        "position": "fixed",
        "top": "0",
        "left": "0",
        "zIndex": "1000",
        "backgroundColor": "#343a40",
        "padding": "0",
    },
)