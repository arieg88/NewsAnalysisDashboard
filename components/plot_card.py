import dash_bootstrap_components as dbc
from dash import dcc, html
from configurations.config import *

# Function to create a card
def create_plot_card(card_number, page_name, placeholder="Select an option"):
    label = page_labels[page_name]
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H1(
                    f"{label}",
                    id={'type': 'category-header'},
                    style={'text-align': 'center'}
                ),
            ),
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    # Top Dropdown
                                    dcc.Dropdown(
                                        id={'type': 'subcategory-dropdown-top-left'},
                                        options=categories[page_name],  # Initially empty
                                        value="sentiment_analysis_per_sentence",  # Default value
                                        clearable=False,
                                        placeholder=placeholder,
                                        style={'text-align': 'center'}
                                    ),
                                    # Output for Top Dropdown
                                    html.Div(id={'type': 'output-top-left'}),
                                ],
                                width=6,  # Left Column takes half the width
                                id={'type': 'top-left-panel'},
                            ),
                            dbc.Col(
                                [
                                    # Top Dropdown
                                    dcc.Dropdown(
                                        id={'type': 'subcategory-dropdown-top-right'},
                                        options=categories[page_name],  # Initially empty
                                        value="sentiment_analysis_per_sentence",  # Default value
                                        clearable=False,
                                        placeholder=placeholder,
                                        style={'text-align': 'center'}
                                    ),
                                    # Output for Top Dropdown
                                    html.Div(id={'type': 'output-top-right'}),
                                ],
                                width=6,  # Right Column takes half the width
                                id={'type': 'top-right-panel'},
                            ),
                        ],
                        id={'type': 'top-panel'},
                    ),
                    dbc.Row(
                        [     
                            # Bottom Dropdown
                            dcc.Dropdown(
                                id={'type': 'subcategory-dropdown-bottom'},
                                options=categories[page_name],  # Initially empty
                                value="sentiment_analysis_per_sentence",  # Default value
                                clearable=False,
                                placeholder=placeholder,
                                style={'text-align': 'center'}
                            ),
                            # Output for Bottom Dropdown
                            html.Div(id={'type': 'output-bottom'}),
                        ],
                        id={'type': 'bottom-panel'},
                    ),
                ],
                id={'type': 'card-body'},
            ),
        ],
        className="mb-4",
    )
