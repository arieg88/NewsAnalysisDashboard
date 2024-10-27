import dash_bootstrap_components as dbc
from dash import html
from configurations.config import *

# Define the navbar
navbar = dbc.Navbar(
    dbc.Nav(
        [
            dbc.NavLink(
                html.Img(src=project_logo, style={"width": "100%", "maxHeight": "10vh", "marginTop": "10px"}),
                active="exact",
                style={"backgroundColor": "transparent", "border": "none"},
                id="logo-link"
            ),
            html.Br(),
            dbc.Stack([
                dbc.NavLink(
                    html.Img(src=home_icon, style={"width": "50%", "maxHeight": "10vh"}),
                    href="/",
                    active="exact",
                    style={"backgroundColor": "transparent", "border": "none"},
                    id="home-link"
                ),
                dbc.Tooltip("Home Page", target="home-link", placement="right"),
                html.Br(),
                dbc.NavLink(
                    html.Img(src=article_icon, style={"width": "50%", "maxHeight": "10vh"}),
                    href="/article_analysis",
                    active="exact",
                    style={"backgroundColor": "transparent", "border": "none"},
                    id="article-link"
                ),
                dbc.Tooltip("Article Analysis", target="article-link", placement="right"),
                html.Br(),
                dbc.NavLink(
                    html.Img(src=sen_and_tren_icon, style={"width": "50%", "maxHeight": "10vh"}),
                    href="/trends_and_patterns",
                    active="exact",
                    style={"backgroundColor": "transparent", "border": "none"},
                    id="sentiment-link"
                ),
                dbc.Tooltip("Data Trends & Patterns", target="sentiment-link", placement="right"),
            ]),
            dbc.NavLink(
                html.Img(src=user_icon, style={"width": "100%", "maxHeight": "10vh", "marginBottom": "10px"}),
                href="/aboutme",
                active="exact",
                style={"backgroundColor": "transparent", "border": "none"},
                id="aboutme-link"
            ),
            dbc.Tooltip("About Me", target="aboutme-link", placement="right"),
        ],
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