from dash import dcc
from dash.dependencies import Input, Output, MATCH
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import *
from plots.trends_and_patterns_plots import *
from components.filters_area import get_filter_values

def get_filtered_df(df, selected_companies=None, selected_authors=None, date_range=None):
    """
    Filters the DataFrame based on selected companies, authors, and date range.

    Parameters:
    df (DataFrame): The original DataFrame to filter.
    selected_companies (list): List of companies to filter by.
    selected_authors (list): List of authors to filter by.
    date_range (tuple): A tuple containing start and end dates for filtering.

    Returns:
    DataFrame: The filtered DataFrame.
    """
    # Create a copy of the original DataFrame to avoid modifying it
    tmp_df = df.copy()
    
    # Apply company filters
    if selected_companies:
        tmp_df = tmp_df[tmp_df['Company'].isin(selected_companies)]
    
    # Apply author filters
    if selected_authors:
        tmp_df = tmp_df[tmp_df['Author'].isin(selected_authors)]
    
    # Apply date range filter if provided
    if date_range and len(date_range) == 2:
        start_date, end_date = date_range
        if start_date and end_date:
            start_date_utc = pd.Timestamp(start_date).tz_localize('UTC')
            end_date_utc = pd.Timestamp(end_date).tz_localize('UTC')
            tmp_df = tmp_df[(tmp_df['Date'] >= start_date_utc) & (tmp_df['Date'] <= end_date_utc)]

    return tmp_df

def update_trends_and_patterns_output(subcategory_value, dfs, selected_companies, selected_authors, date_range):
    """
    Updates the output based on the selected subcategory value and filters.

    Parameters:
    subcategory_value (str): The selected subcategory for plotting.
    dfs (dict): Dictionary of DataFrames used in the dashboard.
    selected_companies (list): List of selected companies from filters.
    selected_authors (list): List of selected authors from filters.
    date_range (tuple): A tuple of selected start and end dates.

    Returns:
    Plot or str: The generated plot or a message if no option is selected.
    """
    # Filter the final DataFrame based on selected filters
    final_df = get_filtered_df(dfs['final_df'], selected_companies, selected_authors, date_range)

    # Generate plots based on the selected subcategory
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

    return 'Select an option to see the plot.'

def register_trends_and_patterns_output_update(app, dfs):
    """
    Registers callbacks to update the output of trends and patterns plots based on user selections.

    Parameters:
    app: The Dash app instance.
    dfs (dict): Dictionary of DataFrames used in the dashboard.
    """
    # Callback for generating plots based on selected subcategory
    @app.callback(
        Output({'type': 'output-top-left', 'page': trends_page_name}, 'children'),
        [Input({'type': 'subcategory-dropdown-top-left', 'page': trends_page_name}, 'value'),
         Input('page-load-trigger', 'data'),
         *get_filter_values(trends_page_name)]
    )
    def update_top_left_output(subcategory_value, page_name, selected_companies, selected_authors, date_range):
        """
        Updates the top left output area based on user selections from the dropdown.

        Parameters:
        subcategory_value (str): The selected subcategory from the dropdown.
        page_name: Data related to the page load trigger.
        selected_companies (list): List of selected companies from filters.
        selected_authors (list): List of selected authors from filters.
        date_range (tuple): A tuple of selected start and end dates.

        Returns:
        Plot: The generated plot for the top left output.
        """
        return update_trends_and_patterns_output(subcategory_value, dfs, selected_companies, selected_authors, date_range)

    @app.callback(
        Output({'type': 'output-top-right', 'page': trends_page_name}, 'children'),
        [Input({'type': 'subcategory-dropdown-top-right', 'page': trends_page_name}, 'value'),
         Input('page-load-trigger', 'data'),
         *get_filter_values(trends_page_name)]  # Use State here instead of Input
    )
    def update_top_right_output(subcategory_value, page_name, selected_companies, selected_authors, date_range):
        """
        Updates the top right output area based on user selections from the dropdown.

        Parameters:
        subcategory_value (str): The selected subcategory from the dropdown.
        page_name: Data related to the page load trigger.
        selected_companies (list): List of selected companies from filters.
        selected_authors (list): List of selected authors from filters.
        date_range (tuple): A tuple of selected start and end dates.

        Returns:
        Plot: The generated plot for the top right output.
        """
        return update_trends_and_patterns_output(subcategory_value, dfs, selected_companies, selected_authors, date_range)

    @app.callback(
        Output({'type': 'output-bottom', 'page': trends_page_name}, 'children'),
        [Input({'type': 'subcategory-dropdown-bottom', 'page': trends_page_name}, 'value'),
         Input('page-load-trigger', 'data'),
         *get_filter_values(trends_page_name)]  # Use State here instead of Input
    )
    def update_bottom_output(subcategory_value, page_name, selected_companies, selected_authors, date_range):  
        """
        Updates the bottom output area based on user selections from the dropdown.

        Parameters:
        subcategory_value (str): The selected subcategory from the dropdown.
        page_name: Data related to the page load trigger.
        selected_companies (list): List of selected companies from filters.
        selected_authors (list): List of selected authors from filters.
        date_range (tuple): A tuple of selected start and end dates.

        Returns:
        Plot: The generated plot for the bottom output.
        """
        return update_trends_and_patterns_output(subcategory_value, dfs, selected_companies, selected_authors, date_range)
