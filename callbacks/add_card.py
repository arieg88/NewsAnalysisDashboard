from dash.dependencies import Input, Output, State, MATCH
from configurations.config import *
from components.navbar import *
from components.plot_card import * 
from utils import load_dfs

def register_add_card(app):
    # Callback to add new card containers
    @app.callback(
        [Output("cards-container", "children"),
         Output("add-card-icon", "style")],
        Input("add-card-icon", "n_clicks"),
        State("cards-container", "children"),
    )
    def add_card(n_clicks, current_cards):
        num_cards = len(current_cards)
        display_plus = {"textAlign": "center", "marginTop": "20px", "display": "block"} if num_cards < 5 else {"display": "none"}
        if n_clicks is None or num_cards >= 5: 
            return current_cards, display_plus
        new_card_number = num_cards + 1
        
        return current_cards + [create_card(new_card_number)], display_plus
