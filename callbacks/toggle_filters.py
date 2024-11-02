import dash
from dash.dependencies import Input, Output, MATCH

def register_toggle_filters(app):
    """
    Registers a callback to toggle the visibility of filters and updates the arrow direction.
    
    Parameters:
    app: The Dash app instance.
    """
    @app.callback(
        Output({'style': 'filters-collapse', 'page': MATCH}, 'is_open'),
        Input({'type': 'collapse-filters', 'page': MATCH}, 'n_clicks'),
        prevent_initial_call=True
    )
    def toggle_filters(n_clicks):
        """
        Toggles the filter visibility based on the number of clicks.
        
        Parameters:
        n_clicks: The number of clicks on the filter toggle button.

        Returns:
        bool: True if filters should be open, False otherwise.
        """
        if n_clicks is None:
            return False  # Default state

        is_open = n_clicks % 2 == 1  # Odd clicks open the filters
        return is_open
