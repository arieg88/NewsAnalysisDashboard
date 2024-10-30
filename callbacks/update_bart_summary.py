from dash import dcc, html
from dash.dependencies import Input, Output, MATCH

# Importing configurations, navbar, and plot card components
from configurations.config import *
from components.navbar import *
from components.plot_card import *
from plots.article_plots import *

def register_update_bart_summary(app, dfs):
    """Register a callback to update the BART summary area based on selected articles.

    Args:
        app: The Dash application instance.
        dfs: A dictionary of DataFrames used in the application.

    Returns:
        None
    """
    # Callback for generating plots based on selected article
    @app.callback(
        Output({'type': 'bart-summary-area', 'page': article_page_name}, 'children'),
        Input({'type': 'article-selection-dropdown', 'page': article_page_name}, 'value')
    )
    def update_bart_summary(article_index):
        """Return the BART summary for the selected article index.

        Args:
            article_index: The index of the selected article.

        Returns:
            html.P: An HTML paragraph containing the BART summary.
        """
        if article_index is None:
            article_index = 0  # Default to the first article if none is selected
        return html.P(str(dfs['final_df'].loc[article_index, 'Bart_Summary']))
