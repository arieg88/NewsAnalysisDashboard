from dash.dependencies import Input, Output
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import *
from components.filters_area import get_filter_values  # Import your filter values function
import pandas as pd

def register_update_article_selection(app, dfs):
    """Register callback to update the article selection dropdown based on the DataFrame (dfs)."""
    @app.callback(
        Output({'type': 'article-selection-dropdown', 'page': article_page_name}, 'options'),
        [
            Input('page-load-trigger', 'data'),  # This will be triggered on page load
            *get_filter_values(article_page_name)  # Add filter inputs dynamically here
        ]
    )
    def update_article_selection_dropdown(_, selected_companies, selected_authors, date_range):
        """Update the article selection dropdown based on selected filters."""
        if 'final_df' in dfs:
            df = dfs['final_df']  # Start with the full DataFrame
            # Apply filters
            if selected_companies:
                df = df[df['Company'].isin(selected_companies)]
            if selected_authors:
                df = df[df['Author'].isin(selected_authors)]
            # Apply date range filter
            if date_range and len(date_range) == 2:
                start_date, end_date = date_range
                if start_date and end_date:
                    start_date_utc = pd.Timestamp(start_date).tz_localize('UTC')
                    end_date_utc = pd.Timestamp(end_date).tz_localize('UTC')
                    df = df[(df['Date'] >= start_date_utc) & (df['Date'] <= end_date_utc)]

            # Update options for the article selection dropdown
            options = [{'label': title, 'value': index} for index, title in enumerate(df['Title'])]

            return options  # Return the filtered options
        return []  # Return an empty list if DataFrame is not available