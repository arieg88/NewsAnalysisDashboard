import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from .filters_area import get_filters_area
from configurations.config import *
import dash

# Function to create a card with filters
def create_article_selection_card(placeholder="Select an article"):
    return dbc.Card(
        [
            dbc.CardHeader(
                    html.H1(
                        "Explore The Articles",
                        id={'type': 'article-header-card-header', 'page': article_page_name},
                        style={'text-align': 'center'}
                    ),
            ),
            dbc.CardHeader([
                        html.P(
                            "📊 Article Analysis Overview 📊",
                            style={'fontWeight': 'bold', 'fontSize': '1.5em'}
                        ),
                        html.P(
                            "Welcome to the Article Analysis page, where you can dive deep into the details of a selected article! This page provides tools to explore each article's content and sentiment through interactive plots and visual summaries. 📰"
                        ),
                        html.P(
                            "Each plot offers a unique lens into the article’s tone, emotion, and structure. Whether you're interested in a breakdown of entities, a sentiment map, or an emotional journey throughout the text, you’ll get valuable insights into each article's emotional and analytical landscape."
                        ),
                        html.P(
                            "Additionally, you can filter articles by company, date, and author to quickly find what you need, with more search options coming soon! 🔍"
                        )
                    ]
                ),
            dbc.CardBody(
                [
                    # Dropdown for article selection
                    dcc.Dropdown(
                        id={'type': 'article-selection-dropdown', 'page': article_page_name},
                        options=[],  # Initially empty, will be populated dynamically
                        clearable=False,
                        value=0,
                        placeholder=placeholder,
                        style={'text-align': 'center'}
                    ),
                    html.Div(
                        get_filters_area(article_page_name),
                    ),
                ],
                id={'type': 'article-selection-card-body', 'page': article_page_name},
            ),
            dbc.CardBody(
                [
                    html.H2('Article Info:'),
                    dbc.Row(id={'type': 'article-info-area', 'page': article_page_name}),
                    html.H2('Bart Summary:'),
                    html.Br(),
                    html.Div(id={'type': 'bart-summary-area', 'page': article_page_name}),
                ],
                id={'type': 'bart-summary-panel', 'page': article_page_name}

            )
        ],
        className="mb-4",
    )

# Register callback to toggle the collapsible advanced filters
    # @app.callback(
    #     Output({'type': 'advanced-filters-collapse'}, 'is_open'),
    #     Input({'type': 'toggle-advanced-filters-btn'}, 'n_clicks'),
    #     [dash.dependencies.State({'type': 'advanced-filters-collapse'}, 'is_open')],
    # )
    # def toggle_advanced_filters(n_clicks, is_open):
    #     if n_clicks:
    #         return not is_open
    #     return is_open
