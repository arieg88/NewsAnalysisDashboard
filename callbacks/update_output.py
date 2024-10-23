from dash import dcc
from dash.dependencies import Input, Output, MATCH
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import * 
from plots.article_plots import *

def register_update_output(app, dfs):
    # Callback for generating plots based on selected subcategory
    @app.callback(
        Output({'type': 'output', 'index': MATCH}, 'children'),
        Input({'type': 'subcategory-dropdown','index': MATCH}, 'value'),
    )
    def update_output(subcategory_value):
        if subcategory_value == "article_count":
            return generate_article_count_plot(dfs['final_df'])
        return "Select an option to see the plot."


