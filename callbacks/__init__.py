from .update_bart_summary import register_update_bart_summary
from .update_authors import register_update_authors_list
from .update_article_info import register_update_article_info
from .update_article_output import register_article_output_update
from .update_trends_and_patterns_output import register_trends_and_patterns_output_update
from .update_article_selection import register_update_article_selection
from .toggle_filters import register_toggle_filters
from .add_card import register_add_card

def register_callbacks(app, dfs):
    """
    Registers all callback functions for the dashboard to the app instance.
    
    Parameters:
    app: The Dash app instance.
    dfs: A dictionary containing the DataFrames used in the dashboard.
    """
    register_update_bart_summary(app, dfs)
    register_update_article_selection(app, dfs)
    register_update_authors_list(app, dfs)
    register_article_output_update(app, dfs)
    register_update_article_info(app, dfs)
    register_trends_and_patterns_output_update(app, dfs)
    register_toggle_filters(app)
    register_add_card(app)