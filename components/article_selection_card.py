import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from .filters_area import get_filters_area
import dash

# Function to create a card with filters
def create_article_selection_card(placeholder="Select an article"):
    return dbc.Card(
        [
            dbc.CardHeader(
                html.H1(
                    "Explore The Articles",
                    id={'type': 'article-header-card-header'},
                    style={'text-align': 'center'}
                ),
            ),
            dbc.CardBody(
                [
                    # Dropdown for article selection
                    dcc.Dropdown(
                        id={'type': 'article-selection-dropdown'},
                        options=[],  # Initially empty, will be populated dynamically
                        clearable=False,
                        value=0,
                        placeholder=placeholder,
                        style={'text-align': 'center'}
                    ),
                    html.Div(
                        get_filters_area(),
                    ),
                ],
                id={'type': 'article-selection-card-body'},
            ),
            dbc.CardBody(
                [
                    html.H2('Bart Summary:'),
                    html.Br(),
                    html.Div(id={'type': 'bart-summary-area'}),
                ],
                id={'type': 'bart-summary-panel'}

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
