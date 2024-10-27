from dash.dependencies import Input, Output, MATCH
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import *
from components.filters_area import get_filter_values  # Import your filter values function
import pandas as pd

# Register callback to update the article selection dropdown based on the DataFrame (dfs)
def register_update_authors_list(app, dfs):
    @app.callback(
        Output({'type': 'author-selection-dropdown', "page": MATCH}, 'options'),
        Input('page-load-trigger', 'data'),  # This will be triggered on page load
    )
    def update_authors_list(_):
        # Extract article titles from the DataFrame
        if 'final_df' in dfs:
            df = dfs['final_df']  # Start with the full DataFrame
            authors = df['Author'].unique().tolist()

            return [{'label': author, 'value': author} for author in authors]
        return []
