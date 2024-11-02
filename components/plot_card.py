import dash_bootstrap_components as dbc
from dash import dcc, html
from configurations.config import *

# Function to create a card for visualizations on a given page
def create_plot_card(page_name, index=0, placeholder='Select an option'):
    """
    Creates a plot card layout with a single dropdown and output div.
    
    Parameters:
    - page_name: The name of the page to which the card belongs.
    - placeholder: The placeholder text for the dropdown (default: 'Select an option').

    Returns:
    - A Dash Bootstrap Card containing the initial layout with one dropdown-output pair.
    """

    label = page_labels[page_name]
    default_value = 'sentiment_distribution_by_company' if page_name == 'trends_and_patterns_page' else 'positive_vs_negative_sentence_count'

    return dbc.Card(
        [
            # dbc.CardHeader(
            #     html.H1(
            #         f'{label}',  # Header for the card
            #         id={'type': 'category-header', 'page': page_name},
            #         style={'text-align': 'center'}
            #     ),
            # ),
            dbc.CardBody(
                [
                    # Initial Dropdown and output div
                    dbc.Row(
                        [
                            dcc.Dropdown(
                                id={'type': 'subcategory-dropdown', 'page': page_name, 'index': index},
                                options=categories[page_name],  # Options based on the page categories
                                value=default_value,
                                clearable=False,
                                placeholder=placeholder,
                                style={'text-align': 'center'}
                            ),
                            html.Div(id={'type': 'output-div', 'page': page_name, 'index': index}),
                        ],
                        id={'type': 'panel-row', 'page': page_name, 'index': index},
                    ),
                ],
                id={'type': 'card-body', 'page': page_name, 'index': index},
            ),
        ],
        className='mb-4',  # Bootstrap margin bottom class
    )
