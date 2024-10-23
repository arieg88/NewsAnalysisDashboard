from dash.dependencies import Input, Output, State, MATCH
from configurations.config import *
from components.navbar import *
from components.plot_card import *
import dash

def register_add_card(app):
    # Callback to add new card containers
    @app.callback(
        [Output("cards-container", "children"),
         Output("add-card-icon", "style")],
        Input("add-card-icon", "n_clicks"),
        State("cards-container", "children"),
    )
    def add_card(n_clicks, current_cards):
        # Determine the current page to adjust category based on URL
        ctx = dash.callback_context
        if not ctx.triggered:
            return current_cards, {}
        
        # Get the current page path from `ctx` and determine the category
        page_path = ctx.request.path  # Extract current path
        category = determine_category_from_path(page_path)
        
        num_cards = len(current_cards)
        display_plus = {"textAlign": "center", "marginTop": "20px", "display": "block"} if num_cards < 5 else {"display": "none"}
        if n_clicks is None or num_cards >= 5: 
            return current_cards, display_plus
        
        new_card_number = num_cards + 1
        
        return current_cards + [create_plot_card(new_card_number, category)], display_plus


def determine_category_from_path(page_path):
    """
    Function to determine the category based on the current page path.
    """
    if 'article_analysis' in page_path:
        return 'article_page'
    elif 'sentiment_analysis' in page_path:
        return 'sentiment_page'
    elif 'emotion_analysis' in page_path:
        return 'emotion_page'
    elif 'comparative_analysis' in page_path:
        return 'comparative_page'
    # Add more paths if necessary
    return None
