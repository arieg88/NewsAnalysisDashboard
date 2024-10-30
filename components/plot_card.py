import dash_bootstrap_components as dbc
from dash import dcc, html
from configurations.config import *

# Function to create a card for visualizations on a given page
def create_plot_card(page_name, placeholder='Select an option'):
    """
    Creates a plot card layout with dropdowns for selecting subcategories
    and outputs for visualizations based on the selected options.

    Parameters:
    - page_name: The name of the page to which the card belongs.
    - placeholder: The placeholder text for the dropdowns (default: 'Select an option').
    
    Returns:
    - A Dash Bootstrap Card containing the layout for the selected page.
    """

    label = page_labels[page_name]

    # Default values for the dropdowns based on the page name
    top_left_default_value = 'positive_vs_negative_sentence_count' if page_name == 'article_page' else \
                             'sentiment_distribution_by_company' if page_name == 'trends_and_patterns_page' else None
    top_right_default_value = 'entities_found_in_article' if page_name == 'article_page' else \
                              'plot_monthly_avg_emotion_joy' if page_name == 'trends_and_patterns_page' else None
    bottom_default_value = 'emotional_journey' if page_name == 'article_page' else \
                           'article_count_by_month' if page_name == 'trends_and_patterns_page' else None

    return dbc.Card(
        [
            dbc.CardHeader(
                html.H1(
                    f'{label}',  # Header for the card
                    id={'type': 'category-header', 'page': page_name},
                    style={'text-align': 'center'}
                ),
            ),
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                [
                                    # Top Left Dropdown for subcategory selection
                                    dcc.Dropdown(
                                        id={'type': 'subcategory-dropdown-top-left', 'page': page_name},
                                        options=categories[page_name],  # Options based on the page categories
                                        value=top_left_default_value,
                                        clearable=False,
                                        placeholder=placeholder,
                                        style={'text-align': 'center'}
                                    ),
                                    # Output for the selection from the Top Left Dropdown
                                    html.Div(id={'type': 'output-top-left', 'page': page_name}),
                                ],
                                width=6,  # Left Column takes half the width
                                id={'type': 'top-left-panel', 'page': page_name},
                            ),
                            dbc.Col(
                                [
                                    # Top Right Dropdown for subcategory selection
                                    dcc.Dropdown(
                                        id={'type': 'subcategory-dropdown-top-right', 'page': page_name},
                                        options=categories[page_name],  # Options based on the page categories
                                        value=top_right_default_value,
                                        clearable=False,
                                        placeholder=placeholder,
                                        style={'text-align': 'center'}
                                    ),
                                    # Output for the selection from the Top Right Dropdown
                                    html.Div(id={'type': 'output-top-right', 'page': page_name}),
                                ],
                                width=6,  # Right Column takes half the width
                                id={'type': 'top-right-panel', 'page': page_name},
                            ),
                        ],
                        id={'type': 'top-panel', 'page': page_name},
                    ),
                    dbc.Row(
                        [
                            # Bottom Dropdown for subcategory selection
                            dcc.Dropdown(
                                id={'type': 'subcategory-dropdown-bottom', 'page': page_name},
                                options=categories[page_name],  # Options based on the page categories
                                value=bottom_default_value,
                                clearable=False,
                                placeholder=placeholder,
                                style={'text-align': 'center'}
                            ),
                            # Output for the selection from the Bottom Dropdown
                            html.Div(id={'type': 'output-bottom', 'page': page_name}),
                        ],
                        id={'type': 'bottom-panel', 'page': page_name},
                    ),
                ],
                id={'type': 'card-body', 'page': page_name},
            ),
        ],
        className='mb-4',  # Bootstrap margin bottom class
    )
