from configurations.config import *
from components.navbar import *
from components.plot_card import create_plot_card  # Import the plot card creation function
from dash import Input, Output, State, MATCH

def register_add_card(app):
    @app.callback(
        Output({"type": "cards-container", "page": MATCH}, "children"),
        Input({"type": "add-panel-button", "page": MATCH}, "n_clicks"),
        State({"type": "cards-container", "page": MATCH}, "children"),
        Input({"type": "cards-container", "page": MATCH}, "id"),
        
        # State({"type": "add-panel-button", "page": MATCH}, "id"),
        prevent_initial_call=True,
    )
    def add_panel(n_clicks, current_children, cards_conatiner_id):
        page_name = cards_conatiner_id["page"]

        if n_clicks is None:
            return current_children

        # Initialize current_children if None
        if current_children is None:
            current_children = []

        # Calculate the current index for the new card
        current_index = len(current_children)
        # Create a new plot card with the current index
        # page_name = current_children[0]["props"]["children"][0]["props"]["children"]["props"]["id"]['page']
        new_plot_card = create_plot_card(page_name=page_name, index=current_index)

        # Append the new plot card, followed by the `+` button, and return the updated list
        return current_children[:-1] + [new_plot_card, current_children[-1]]
