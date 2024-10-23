from .add_card_button import register_toggle_add_card_button
from .add_card import register_add_card
from .subcategory_options import register_update_subcategory_dropdown
from .update_output import register_update_output

def register_callbacks(app, dfs):
    register_toggle_add_card_button(app)
    register_add_card(app)
    register_update_subcategory_dropdown(app)
    register_update_output(app, dfs)