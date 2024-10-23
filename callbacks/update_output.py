from dash import dcc
from dash.dependencies import Input, Output, MATCH
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import * 
from plots.article_plots import *

def update_output(subcategory_value, dfs, article_id=0):
    if subcategory_value == "sentiment_analysis_per_sentence":
        return plot_sentiment_analysis_per_sentence(dfs['final_df'], article_id)
    elif subcategory_value == "positive_vs_negative_sentence_count":
        return plot_positive_vs_negative_sentence_count(dfs['final_df'], article_id)
    elif subcategory_value == "entities_found_in_article":
        return plot_entities_found_in_article(dfs['entities_df'], article_id)
    elif subcategory_value == "entity_types_breakdown":
        return plot_entity_types_breakdown(dfs['entities_df'], article_id)
    elif subcategory_value == "emotion_distribution":
        return plot_emotion_distribution(dfs['final_df'], article_id)
    return "Select an option to see the plot."


def register_update_outputs(app, dfs):
    # Callback for generating plots based on selected subcategory
    @app.callback(
        Output({'type': f'output-top-left'}, 'children'),
        [Input({'type': f'subcategory-dropdown-top-left'}, 'value'),
         Input({'type': 'article-selection-dropdown'}, 'value')]
    )
    def update_top_left_output(subcategory_value, article_id):
        return update_output(subcategory_value, dfs, article_id)

    @app.callback(
        Output({'type': f'output-top-right'}, 'children'),
        [Input({'type': f'subcategory-dropdown-top-right'}, 'value'),
        Input({'type': 'article-selection-dropdown'}, 'value')]
    )
    def update_top_right_output(subcategory_value, article_id):  
        return update_output(subcategory_value, dfs, article_id)

    @app.callback(
        Output({'type': 'output-bottom'}, 'children'),
        [Input({'type': 'subcategory-dropdown-bottom'}, 'value'),
        Input({'type': 'article-selection-dropdown'}, 'value')]
    )
    def update_bottom_output(subcategory_value, article_id):  
        return update_output(subcategory_value, dfs, article_id)
