import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output, State, MATCH
import pandas as pd
import plotly
import plotly.express as px
from configurations.config import *
from components.navbar import *
from components.plot_card import * 
from layouts.App_layout import *
from utils import load_dfs
import callbacks

# Load the DataFrame
df = pd.read_csv("./data/final_df.csv")

dfs = load_dfs()

# # Ensure that the Agg_Finbert_aggregated_score is numeric, converting if necessary
# df['Agg_Finbert_aggregated_score'] = pd.to_numeric(df['Agg_Finbert_aggregated_score'], errors='coerce')

# Now you can calculate the mean safely, grouping by sentiment
# finbert_scores = df.groupby('Agg_Finbert_overall_sentiment')['Agg_Finbert_aggregated_score'].mean().reset_index()
# finbert_scores.columns = ['Sentiment', 'Score']


# Include Font Awesome and Bootstrap in external stylesheets
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css",
]

# Create the Dash app instance
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True)

app.layout = get_app_layout()

callbacks.register_callbacks(app, dfs)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)