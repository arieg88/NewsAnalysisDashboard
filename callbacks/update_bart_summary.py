from dash import dcc
from dash.dependencies import Input, Output, MATCH
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import * 
from plots.article_plots import *

def register_update_bart_summary(app, dfs):
    # Callback for generating plots based on selected subcategory
    @app.callback(
        Output({'type': 'bart-summary-area'}, 'children'),
        Input({'type': 'article-selection-dropdown'}, 'value')
    )
    def update_bart_summary(article_index):
        if article_index == None:
            article_index = 0
        return html.P(str(dfs['final_df'].loc[article_index, 'Bart_Summary']))
