from .app_layout import get_app_layout
from components.article_selection_card import create_article_selection_card
import dash
from dash import html, dcc
from configurations.config import *

# Register the page with Dash
dash.register_page(__name__, path='/article_analysis')

# Get the label for the article page from the configuration
label = page_labels[article_page_name]

def layout():
    """
    Define the layout for the article analysis page.

    Returns:
        html.Div: A Dash HTML component representing the layout of the article analysis page.
    """
    
    # Create the top section of the page with article selection options
    page_top = create_article_selection_card()

    return html.Div(
        children=[
            # Store component to trigger page load
            dcc.Store(id='page-load-trigger', data='article_analysis'),  # This triggers the page load
            
            # Main app layout with the article selection card at the top
            get_app_layout(article_page_name, page_top=page_top, placeholder='Select article by...')
        ],
        id={'type': 'article-main-div', "page": "article_page_name"}  # Unique ID for the main div of the article page
    )
