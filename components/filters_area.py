import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output
import dash
from configurations.config import *

def get_filter_values(page_name):
    return [
        Input({'type': 'company-selection-dropdown', "page": page_name}, 'value'),  # Company filter
        Input({'type': 'author-selection-dropdown', "page": page_name}, 'value'),   # Author filter
        (Input({'type': 'article-date-picker', "page": page_name}, 'start_date'),    # Start date for date range
        Input({'type': 'article-date-picker', "page": page_name}, 'end_date') ),      # End date for date range
    ]


def get_filters_area(page_name):
    return dbc.Row(
        [

            html.Label('Filter By:', style={'font-weight': 'bold'}),
            # Row for Company, Date, and Author filters
            dbc.Row(
                [
                    # Filter by company
                    dbc.Col(
                        html.Div(
                            [
                                html.Label("Company", style={'font-weight': 'bold'}),
                                dcc.Dropdown(
                                    id={'type': 'company-selection-dropdown', 'page': page_name},
                                    options=companies, 
                                    placeholder="Select a company",
                                    clearable=True,
                                    multi=True,
                                    style={'width': '100%'}
                                ),
                            ],
                        ),
                        width=4,  # Adjust the column width
                    ),

                    # Filter by author
                    dbc.Col(
                        html.Div(
                            [
                                html.Label("Author", style={'font-weight': 'bold'}),
                                dcc.Dropdown(
                                    id={'type': 'author-selection-dropdown', 'page': page_name},
                                    options=[],  # To be populated dynamically
                                    placeholder="Select an author",
                                    clearable=True,
                                    multi=True,
                                    style={'width': '100%'}
                                ),
                            ]
                        ),
                        width=4,  # Adjust the column width
                    ),
                    # Filter by date (using a cleaner date range picker)
                    dbc.Col(
                        html.Div(
                            [
                                html.Label("Date Range", style={'font-weight': 'bold'}),
                                dcc.DatePickerRange(
                                    id={'type': 'article-date-picker', 'page': page_name},
                                    start_date=None,  # Default start date can be set here
                                    end_date=None,    # Default end date can be set here
                                    display_format='YYYY-MM-DD',
                                    style={'width': '100%'}
                                ),
                            ]
                        ),
                        width=4,  # Adjust the column width
                    ),
                ],
                style={'height': '50%'},
                className="mb-4"  # Add margin between filters and other elements
            ),
            
            # # Collapsible advanced filters
            # dbc.Collapse(
            #     dbc.CardBody(
            #         [
            #             html.Label("Advanced Filters", style={'font-weight': 'bold'}),
                        
            #             # Filter by sentiment score
            #             html.Div(
            #                 [
            #                     html.Label("Sentiment Score Range", style={'margin-top': '10px'}),
            #                     dcc.RangeSlider(
            #                         id={'type': 'sentiment-range-slider'},
            #                         min=-1, max=1, step=0.1,
            #                         marks={-1: '-1', 0: '0', 1: '1'},
            #                         value=[-0.5, 0.5]
            #                     ),
            #                 ],
            #                 style={'margin-top': '20px'}
            #             ),
                        
            #             # Filter by article length
            #             html.Div(
            #                 [
            #                     html.Label("Article Length (Number of Sentences)", style={'margin-top': '10px'}),
            #                     dcc.Input(
            #                         id={'type': 'article-length-filter'},
            #                         type='number',
            #                         placeholder="Minimum number of sentences",
            #                         style={'margin-bottom': '10px', 'text-align': 'center'}
            #                     ),
            #                 ],
            #                 style={'margin-top': '20px'}
            #             ),
            #         ]
            #     ),
            #     id={'type': 'advanced-filters-collapse'},
            #     is_open=False  # Initially closed
            # ),
            
            # # Button to toggle advanced filters
            # dbc.Button(
            #     "Advanced Filters",
            #     id={'type': 'toggle-advanced-filters-btn'},
            #     color="link",
            #     style={'margin-top': '10px', 'text-align': 'center'}
            # )
        ],
        id={'style': 'filters-area', 'page': page_name}
    )