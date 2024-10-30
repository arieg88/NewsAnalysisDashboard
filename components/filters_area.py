import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
from configurations.config import *

# Function to get input values for filters based on page name
def get_filter_values(page_name):
    """
    Retrieves the input values for filters on the specified page.

    Args:
        page_name (str): The name of the page for which filter inputs are retrieved.

    Returns:
        list: A list of Dash Input components for the filters.
    """
    return [
        Input({'type': 'company-selection-dropdown', 'page': page_name}, 'value'),  # Company filter
        Input({'type': 'author-selection-dropdown', 'page': page_name}, 'value'),   # Author filter
        (Input({'type': 'article-date-picker', 'page': page_name}, 'start_date'),    # Start date for date range
         Input({'type': 'article-date-picker', 'page': page_name}, 'end_date')),      # End date for date range
    ]

# Function to get input for arrow click event
def get_arrow_click(page_name):
    """
    Retrieves the input for the collapse arrow click event.

    Args:
        page_name (str): The name of the page.

    Returns:
        Input: A Dash Input component for the arrow click.
    """
    return Input({'type': 'collapse-arrow', 'page': page_name}, 'n_clicks')

# Function to create the filters area layout
def get_filters_area(page_name):
    """
    Creates a layout for the filters area with collapsible options.

    Args:
        page_name (str): The name of the page for which filters are created.

    Returns:
        dbc.Col: A Dash Bootstrap Column component containing filter elements.
    """
    return dbc.Col(
        [
            # Filter label with collapsible arrow
            dbc.Row(
                [
                    html.Label('Filter By:', style={'font-weight': 'bold'}),
                    dbc.Button(
                        'Show/Hide Filters', 
                        color='secondary',
                        id={'type': 'collapse-filters', 'page': page_name},
                        n_clicks=0,
                        style={
                            'display': 'inline-block',  # Ensure the button only takes the space of its content
                            'text-align': 'center',      # Center the text inside the button
                            'margin-left': '10px',      # Add margin to separate from the label
                        }
                    )
                ],
                align='left'  # Aligns the label and button
            ),
            # Filters area (initially hidden)
            dbc.Collapse(
                dbc.Col(  # Correctly use dbc.Row and dbc.Col
                    [
                        # Row for Company, Author, and Content filters
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Div(
                                        [
                                            html.Label('Company', style={'font-weight': 'bold'}),
                                            dcc.Dropdown(
                                                id={'type': 'company-selection-dropdown', 'page': page_name},
                                                options=companies, 
                                                placeholder='Select a company',
                                                clearable=True,
                                                multi=True,
                                                style={'width': '100%'}
                                            ),
                                        ],
                                    ),
                                    width=4,  # Adjust column width
                                ),

                                # Filter by author
                                dbc.Col(
                                    html.Div(
                                        [
                                            html.Label('Author', style={'font-weight': 'bold'}),
                                            dcc.Dropdown(
                                                id={'type': 'author-selection-dropdown', 'page': page_name},
                                                options=[],  # To be populated dynamically
                                                placeholder='Select an author',
                                                clearable=True,
                                                multi=True,
                                                style={'width': '100%'}
                                            ),
                                        ]
                                    ),
                                    width=4,  # Adjust column width
                                ),

                                # Filter by content (new text input)
                                dbc.Col(
                                    html.Div(
                                        [
                                            html.Label('Search in Article Content', style={'font-weight': 'bold'}),
                                            dcc.Input(
                                                id={'type': 'content-search-input', 'page': page_name},
                                                type='text',
                                                placeholder='Enter keyword(s) to search',
                                                style={'width': '100%'}
                                            ),
                                        ]
                                    ),
                                    width=4,  # Adjust column width
                                ),
                            ],
                            className='mb-4'  # Margin below the row
                        ),
                        # Row for Date Range Picker
                        dbc.Row(
                            [
                                dbc.Col(
                                    html.Div(
                                        [
                                            html.Label('Date Range', style={'font-weight': 'bold'}),
                                            dcc.DatePickerRange(
                                                id={'type': 'article-date-picker', 'page': page_name},
                                                start_date=None,  # Default start date can be set here
                                                end_date=None,    # Default end date can be set here
                                                display_format='YYYY-MM-DD',
                                                style={'width': '100%'}
                                            ),
                                        ]
                                    ),
                                    width=12,  # Full width for the date picker
                                ),
                            ],
                            className='mb-4'  # Margin below the date picker
                        ),
                    ]
                ),
                id={'style': 'filters-collapse', 'page': page_name},
                is_open=False  # Initially closed
            )
        ],
        id={'style': 'filters-area', 'page': page_name}
    )
