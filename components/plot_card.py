import dash_bootstrap_components as dbc
from dash import dcc, html
from configurations.config import *

# Function to create a card
def create_plot_card(page_name, placeholder="Select an option"):
    label = page_labels[page_name]

    top_left_default_value = "positive_vs_negative_sentence_count" if page_name =='article_page' else \
                                "sentiment_distribution_by_company" if page_name == 'trends_and_patterns_page' else None
    top_right_default_value = "entities_found_in_article"if page_name =='article_page' else \
                                "plot_monthly_avg_emotion_joy" if page_name == 'trends_and_patterns_page'  else None
    bottom_default_value = "emotional_journey"if page_name =='article_page' else \
                                "article_count_by_month" if page_name == 'trends_and_patterns_page'  else None

    return dbc.Card(
        [
            dbc.CardHeader(
                html.H1(
                    f"{label}",
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
                                    # Top Dropdown
                                    dcc.Dropdown(
                                        id={'type': f'subcategory-dropdown-top-left', 'page': page_name},
                                        options=categories[page_name],  # Initially empty
                                        value=top_left_default_value,
                                        clearable=False,
                                        placeholder=placeholder,
                                        style={'text-align': 'center'}
                                    ),
                                    # Output for Top Dropdown
                                    html.Div(id={'type': 'output-top-left', 'page': page_name}),
                                ],
                                width=6,  # Left Column takes half the width
                                id={'type': f'top-left-panel', 'page': page_name},
                            ),
                            dbc.Col(
                                [
                                    # Top Dropdown
                                    dcc.Dropdown(
                                        id={'type': f'subcategory-dropdown-top-right', 'page': page_name},
                                        options=categories[page_name],  # Initially empty
                                        value=top_right_default_value,
                                        clearable=False,
                                        placeholder=placeholder,
                                        style={'text-align': 'center'}
                                    ),
                                    # Output for Top Dropdown
                                    html.Div(id={'type': f'output-top-right', 'page': page_name}),
                                ],
                                width=6,  # Right Column takes half the width
                                id={'type': f'top-right-panel', 'page': page_name},
                            ),
                        ],
                        id={'type': f'top-panel', 'page': page_name},
                    ),
                    dbc.Row(
                        [     
                            # Bottom Dropdown
                            dcc.Dropdown(
                                id={'type': f'subcategory-dropdown-bottom', 'page': page_name},
                                options=categories[page_name],  # Initially empty
                                value=bottom_default_value,
                                clearable=False,
                                placeholder=placeholder,
                                style={'text-align': 'center'}
                            ),
                            # Output for Bottom Dropdown
                            html.Div(id={'type': f'output-bottom', 'page': page_name}),
                        ],
                        id={'type': f'bottom-panel', 'page': page_name},
                    ),
                ],
                id={'type': f'card-body', 'page': page_name},
            ),
        ],
        className="mb-4",
    )
