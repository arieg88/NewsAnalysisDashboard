from dash.dependencies import Input, Output
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import *
from components.filters_area import get_filter_values  # Import your filter values function
import pandas as pd

# Register callback to update the article selection dropdown based on the DataFrame (dfs)
def register_article_selection_card(app, dfs):
    @app.callback(
        Output({'type': 'article-selection-dropdown'}, 'options'),
        [
            Input('page-load-trigger', 'data'),  # This will be triggered on page load
            *get_filter_values()  # Add filter inputs dynamically here
        ]
    )
    def update_article_selection_dropdown(_, selected_companies, selected_authors, date_range):
        # Extract article titles from the DataFrame
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


            # Get unique article titles after filtering
            unique_titles_with_ids = df.groupby('Title')['id'].first().reset_index()
            article_titles = unique_titles_with_ids['Title'].tolist()
            article_ids = unique_titles_with_ids['id'].tolist()
            # Return the titles as options for the dropdown
            return [{'label': title, 'value': article_id} for title, article_id in zip(article_titles, article_ids)]
        return []
