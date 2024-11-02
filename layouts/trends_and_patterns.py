from .app_layout import get_app_layout
from components.trends_and_patterns_selection_card import create_trends_and_data_card
import dash
from dash import html, dcc
from configurations.config import *

dash.register_page(__name__, path='/trends_and_patterns')

page_name = trends_page_name
label = page_labels[page_name]

def layout():
    """
    Layout for the Trends and Patterns page.

    This function creates the layout for the Trends and Patterns page of the 
    Corporate News Analysis Dashboard. It initializes the page with the 
    trends and data selection card, and sets up a storage component to 
    trigger the page load.

    Returns:
        html.Div: The layout of the Trends and Patterns page.
    """
    page_top = create_trends_and_data_card()

    return html.Div(
        children=[
            dcc.Store(id='page-load-trigger', data='trends_and_patterns'),  # This triggers the page load
            get_app_layout(page_name, page_top=page_top, placeholder='Select article by...')
        ],
        id={'type': 'article-main-div'}
    )
