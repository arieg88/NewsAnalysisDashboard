import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from .filters_area import get_filters_area
from configurations.config import *
import dash

# Function to create a card with filters
def create_trends_and_data_card(placeholder="Select an option"):
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H1(
                    "Data Trends & Patterns",
                    id={'type': 'sentiment-header-card-header', "page": trends_page_name},
                    style={'text-align': 'center'}
                ),
            ),
            dbc.CardBody(
                [
                    html.P('Something interesting...'),
                    html.Div(
                        get_filters_area(trends_page_name),
                    ),
                ],
                id={'type': 'article-selection-card-body', "page": trends_page_name},
            ),
        ],
        className="mb-4",
    )