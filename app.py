import dash
import dash_bootstrap_components as dbc
from configurations.config import *
from components.navbar import *
from components.plot_card import *
from utils import load_dfs
import callbacks
import os
import matplotlib

# Redirect Matplotlib cache to a temporary location and use non-GUI backend
os.environ['MPLCONFIGDIR'] = './tmp'
matplotlib.use('Agg')  # Non-interactive backend for server use

# Load the DataFrames
dfs = load_dfs()
# Include Font Awesome and Bootstrap in external stylesheets
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css",
]

# Create the Dash app instance
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True, use_pages=True, pages_folder="layouts")

app.layout = dbc.Container(dash.page_container, fluid=True)

callbacks.register_callbacks(app, dfs)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)