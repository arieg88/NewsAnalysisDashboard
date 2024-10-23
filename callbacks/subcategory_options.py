from dash.dependencies import Input, Output, MATCH
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import * 
from utils import load_dfs

def register_update_subcategory_dropdown(app):
    # Update subcategory dropdown based on selected category
    @app.callback(
        Output({'type':'subcategory-dropdown', 'index': MATCH}, 'options'),
        Input({'type': 'category-dropdown', 'index': MATCH}, 'value'),
    )
    def update_subcategory_dropdown(selected_category):
        if selected_category in categories.keys():
            return [{"label": option["label"], "value": option["value"]} for option in categories[selected_category]]

        return []
