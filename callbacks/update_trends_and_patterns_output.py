from dash import dcc
from dash.dependencies import Input, Output, MATCH
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import * 
from plots.trends_and_patterns_plots import *
from components.filters_area import get_filter_values


def get_filtered_df(df, selected_companies=None, selected_authors=None, date_range=None):
    # Apply filters
    tmp_df = df.copy()
    if selected_companies:
        tmp_df = tmp_df[tmp_df['Company'].isin(selected_companies)]
    if selected_authors:
        tmp_df = tmp_df[tmp_df['Author'].isin(selected_authors)]
    # Apply date range filter
    if date_range and len(date_range) == 2:
        start_date, end_date = date_range
        if start_date and end_date:
            start_date_utc = pd.Timestamp(start_date).tz_localize('UTC')
            end_date_utc = pd.Timestamp(end_date).tz_localize('UTC')
            tmp_df = tmp_df[(tmp_df['Date'] >= start_date_utc) & (tmp_df['Date'] <= end_date_utc)]

    return tmp_df


def update_trends_and_patterns_output(subcategory_value, dfs, selected_companies, selected_authors, date_range):
    final_df = get_filtered_df(dfs['final_df'], selected_companies, selected_authors, date_range)

    if subcategory_value == 'article_count_by_month':
        return plot_stacked_article_count_by_month(final_df)
    elif subcategory_value == 'article_count_by_week':
        return plot_stacked_article_count_by_week(final_df)
    elif subcategory_value == 'top_entities_by_month':
        return plot_top_entities_by_month(dfs['entities_df'], final_df)
    elif subcategory_value == 'top_entity_types_by_month':
        return plot_top_entity_types_by_month(dfs['entities_df'], final_df)
    elif subcategory_value == 'sentiment_distribution_by_company':
        return plot_sentiment_distribution_by_company(final_df)
    elif subcategory_value == 'plot_monthly_avg_emotion_joy':
        return plot_monthly_avg_emotion(final_df, 'Emotion_Sum_joy')

    return "Select an option to see the plot."

def register_trends_and_patterns_output_update(app, dfs):
    # Callback for generating plots based on selected subcategory
    @app.callback(
        Output({'type': 'output-top-left', 'page': trends_page_name}, 'children'),
        [Input({'type': 'subcategory-dropdown-top-left', 'page': trends_page_name}, 'value'),
         Input('page-load-trigger', 'data'),
         *get_filter_values(trends_page_name)]
    )
    def update_top_left_output(subcategory_value, page_name, selected_companies, selected_authors, date_range):
        return update_trends_and_patterns_output(subcategory_value, dfs, selected_companies, selected_authors, date_range)

    @app.callback(
        Output({'type': 'output-top-right', 'page': trends_page_name}, 'children'),
        [Input({'type': 'subcategory-dropdown-top-right', 'page': trends_page_name}, 'value'),
        Input('page-load-trigger', 'data'),
        *get_filter_values(trends_page_name)]  # Use State here instead of Input
    )
    def update_top_right_output(subcategory_value, page_name, selected_companies, selected_authors, date_range):
        return update_trends_and_patterns_output(subcategory_value, dfs, selected_companies, selected_authors, date_range)

    @app.callback(
        Output({'type': 'output-bottom', 'page': trends_page_name}, 'children'),
        [Input({'type': 'subcategory-dropdown-bottom', 'page': trends_page_name}, 'value'),
        Input('page-load-trigger', 'data'),
        *get_filter_values(trends_page_name)]  # Use State here instead of Input
    )
    def update_bottom_output(subcategory_value, page_name, selected_companies, selected_authors, date_range):  
        return update_trends_and_patterns_output(subcategory_value, dfs, selected_companies, selected_authors, date_range)
