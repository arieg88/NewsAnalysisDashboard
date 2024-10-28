from dash import dcc
from dash.dependencies import Input, Output, MATCH
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import * 
from plots.article_plots import *
from configurations.config import *

def update_article_output(subcategory_value, dfs, article_id=0):
    if article_id is None:
        article_id = 0
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
    elif subcategory_value == 'emotional_journey':
        return plot_emotional_journey(dfs['emotions_df'], article_id)
    elif subcategory_value == 'emotion_heatmap':
        return plot_emotion_heatmap(dfs['emotions_df'], article_id)
    elif subcategory_value == 'wordcloud':
        return plot_wordcloud(dfs['final_df'], article_id)
    elif subcategory_value == 'comparison_sentence_sentiment':
        return plot_sentence_sentiment(dfs['final_df'], article_id)
    elif subcategory_value == 'narrative_arc':
        return plot_narrative_arc(dfs['emotions_df'], article_id)
    elif subcategory_value == 'article_emotion_radar':
        return plot_emotions_radar(dfs['emotions_df'], article_id)
    return "Select an option to see the plot."


def register_article_output_update(app, dfs):
    # Callback for generating plots based on selected subcategory
    @app.callback(
        Output({'type': 'output-top-left', 'page': article_page_name}, 'children'),
        [Input({'type': 'subcategory-dropdown-top-left', 'page': article_page_name}, 'value'),
         Input('page-load-trigger', 'data'),
         Input({'type': 'article-selection-dropdown', 'page': article_page_name}, 'value')]  # Use State here instead of Input
    )
    def update_top_left_output(subcategory_value, page_name, article_id=None):
        return update_article_output(subcategory_value, dfs, article_id)

    @app.callback(
        Output({'type': 'output-top-right', 'page': article_page_name}, 'children'),
        [Input({'type': 'subcategory-dropdown-top-right', 'page': article_page_name}, 'value'),
        Input('page-load-trigger', 'data'),
        Input({'type': 'article-selection-dropdown', 'page': article_page_name}, 'value')]  # Use State here instead of Input
    )
    def update_top_right_output(subcategory_value, page_name, article_id=None):
        return update_article_output(subcategory_value, dfs, article_id)

    @app.callback(
        Output({'type': 'output-bottom', 'page': article_page_name}, 'children'),
        [Input({'type': 'subcategory-dropdown-bottom', 'page': article_page_name}, 'value'),
        Input('page-load-trigger', 'data'),
        Input({'type': 'article-selection-dropdown', 'page': article_page_name}, 'value')]  # Use State here instead of Input
    )
    def update_bottom_output(subcategory_value, page_name, article_id=None):  
        return update_article_output(subcategory_value, dfs, article_id)