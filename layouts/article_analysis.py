from .app_layout import get_app_layout
from components.article_selection_card import create_article_selection_card
import dash
from dash import html, dcc
from configurations.config import *

dash.register_page(__name__, path='/article_analysis')

page_name = 'article_page'
label = page_labels[page_name]

def layout():
    page_top = create_article_selection_card()

    return html.Div(
        children=[
            dcc.Store(id='page-load-trigger', data=True),  # This triggers the page load
            get_app_layout(page_name, page_top=page_top, placeholder='Select article by...')
        ],
        id={'type': 'article-main-div'}
    )
