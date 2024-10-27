import dash
from dash.dependencies import Input, Output, MATCH

def register_toggle_filters(app):
    # Callback to toggle filter visibility and change arrow direction
    @app.callback(
        Output({'style': 'filters-collapse', 'page': MATCH}, 'is_open'),
        Input({'type': 'collapse-filters', 'page': MATCH}, 'n_clicks'),
        prevent_initial_call=True
    )
    def toggle_filters(n_clicks):
        if n_clicks is None:
            return False, '▼'  # Default state

        is_open = n_clicks % 2 == 1  # Odd clicks open the filters
        
        return is_open
