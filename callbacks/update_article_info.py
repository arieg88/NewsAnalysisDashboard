from dash import dcc
from dash.dependencies import Input, Output, MATCH
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import * 
from plots.article_plots import *

def register_update_article_info(app, dfs):
    # Callback for generating plots based on selected subcategory
    @app.callback(
        Output({'type': 'article-info-area', 'page': article_page_name}, 'children'),
        Input({'type': 'article-selection-dropdown', 'page': article_page_name}, 'value')
    )
    def update_article_summary(article_index):
        if article_index == None:
            article_index = 0

        date_formatted = dfs['final_df'].loc[article_index, 'Date'].strftime('%d/%m/%Y  %H:%M:%S')
        company = dfs['final_df'][dfs['final_df']['Title'] == dfs['final_df'].loc[article_index, 'Title']]['Company']
        return [
            dbc.Col(
            html.Div(
                [
                    html.Label("Author: "),
                    html.P(dfs['final_df'].loc[article_index, 'Author'])
                ],
            ),
            width=4,  # Adjust the column width
            ),
            dbc.Col(
                html.Div(
                    [
                        html.Label("Date (D/M/Y): "),
                        html.P(date_formatted)
                    ],
                ),
                width=4,  # Adjust the column width
            ),
            dbc.Col(
                html.Div(
                    [
                        html.Label("Company (or Companies): "),
                        html.P(", ".join(company.tolist()))
                    ],
                ),
                width=4,  # Adjust the column width
            )
        ]