from dash.dependencies import Input, Output, MATCH
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import * 
from layouts.App_layout import *
from utils import load_dfs

def register_toggle_add_card_button(app):
    # Callback to show/hide CardBody based on category selection
    @app.callback(
        Output({'type': 'collapse-card', 'index': MATCH}, 'is_open'),
        Input({'type': 'category-dropdown', 'index': MATCH}, 'value'),
    )
    def toggle_add_card_button(selected_category):
        return bool(selected_category)  # True if a category is selected, False otherwise
