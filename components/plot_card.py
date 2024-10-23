import dash_bootstrap_components as dbc
from dash import dcc, html
from configurations.config import *

# Function to create a card
def create_card(card_number):
    return dbc.Card(
        [
            dbc.CardHeader(
                dcc.Dropdown(
                    id={'type': 'category-dropdown', 'index': card_number},
                    options=[{"label": option['label'], "value": option['value']} for option in options],
                    value="",  # Default value is empty
                    clearable=False,
                    placeholder="Choose Category",
                    style={'text-align': 'center'}
                ),
            ),
            dbc.Collapse(
                dbc.CardBody(
                    [
                        dcc.Dropdown(
                            id={'type': 'subcategory-dropdown', 'index': card_number},
                            options=[],  # Initially empty
                            value="",  # Default value
                            clearable=False,
                            placeholder="Select an option",
                            style={'text-align': 'center'}
                        ),
                        html.Div(id={'type': 'output', 'index': card_number})
                    ]
                ),
                id={'type': 'collapse-card', 'index': card_number},
                is_open=False,
            ),
        ],
        className="mb-4",
    )