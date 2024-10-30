from dash.dependencies import Input, Output, MATCH
import pandas as pd

# Importing configurations, navbar, and plot card components
from configurations.config import *
from components.navbar import *
from components.plot_card import *

# Register callback to update the author selection dropdown based on the DataFrame (dfs)
def register_update_authors_list(app, dfs):
    @app.callback(
        Output({'type': 'author-selection-dropdown', 'page': MATCH}, 'options'),
        Input('page-load-trigger', 'data')  # This will be triggered on page load
    )
    def update_authors_list(_):
        """Update the author selection dropdown with unique authors from the DataFrame.

        Returns:
            list: A list of dictionaries containing author labels and values.
        """
        # Extract unique authors from the DataFrame
        if 'final_df' in dfs:
            df = dfs['final_df']  # Start with the full DataFrame
            authors = df['Author'].unique().tolist()

            return [{'label': author, 'value': author} for author in authors]
        return []  # Return an empty list if 'final_df' is not found
