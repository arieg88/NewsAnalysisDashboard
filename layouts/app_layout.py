import dash_bootstrap_components as dbc
from dash import html
from configurations.config import *
from components.navbar import *
from components.plot_card import create_plot_card
import dash

# App layout
def get_app_layout(page_name, page_top=None, placeholder="Select an option"):
    """
    Generate the layout for the Dash application.

    Parameters:
        page_name (str): The name of the current page, used to determine which content to display.
        page_top (Optional[html.Div]): Optional content to be displayed at the top of the page.
        placeholder (str): Placeholder text for the plot card when no option is selected.

    Returns:
        html.Div: A Dash HTML component representing the layout of the page.
    """
    
    return html.Div(
        style={"display": "flex", "height": "100vh"},
        children=[
            # Navbar column
            dbc.Col(navbar, width=2, style={"padding": 0}),
            dbc.Col(
                dbc.Container(
                    [
                        # Top content area
                        dbc.Row(dbc.Col(id="page-top-container", children=page_top)),
                        
                        # Cards container for plots
                        dbc.Row(
                            dbc.Col(
                                id={"type": "cards-container", "page": page_name},
                                children=[
                                    create_plot_card(page_name, placeholder=placeholder, index=0),
                                    # Centered "+" button below the card(s) with minimal size
                                    dbc.Row(
                                        dbc.Col(
                                            dbc.Button(
                                                "+",
                                                id={"type": "add-panel-button", "page": page_name},
                                                style={'font-size': '24px', 'margin-top': '15px'},
                                                color='secondary',
                                                outline=True,
                                            ),
                                            width="auto"  # Ensures button only takes up as much space as necessary
                                        ),
                                        justify="center",
                                    ),
                                ]
                            )
                        ),
                    ],
                    style={"marginTop": "20px"},
                ),
                width=10,
            ),
            dbc.Tooltip('Add new plot',
                target={"type": "add-panel-button", "page": page_name},
                placement='right'
            ),
        ],
    )
