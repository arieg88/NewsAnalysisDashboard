# from .add_card_button import register_toggle_add_card_button
from .add_card import register_add_card
# from .subcategory_options import register_update_subcategory_dropdown
from .update_output import register_update_outputs
# from .article_selection import register_update_article_selection
from .update_bart_summary import register_update_bart_summary
from .article_selection_card_callback import register_article_selection_card
from .update_authors import register_update_authors_list

def register_callbacks(app, dfs):
    # register_toggle_add_card_button(app)
    # register_update_article_selection(app, dfs)
    register_add_card(app)
    # register_update_subcategory_dropdown(app)
    register_update_outputs(app, dfs)
    register_update_bart_summary(app, dfs)
    register_article_selection_card(app, dfs)
    register_update_authors_list(app, dfs)