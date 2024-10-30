import dash
import dash_bootstrap_components as dbc
from configurations.config import *
from components.navbar import *
from components.plot_card import *
from utils import load_dfs
import callbacks

# Load the DataFrames using a utility function
dfs = load_dfs()

# Include Font Awesome and Bootstrap in external stylesheets
external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css',
]

# Create the Dash app instance
app = dash.Dash(__name__, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True, use_pages=True, pages_folder='layouts')

# Define the layout of the app
app.layout = dbc.Container(dash.page_container, fluid=True)

# Register the callbacks for the app
callbacks.register_callbacks(app, dfs)
server = app.server

# Run the app if this script is executed directly
if __name__ == '__main__':
    host = '0.0.0.0'
    port = 8000
    app.run(host=host, port=port, debug=False)
