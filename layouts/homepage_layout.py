from dash import html, dcc
import dash_bootstrap_components as dbc
from components.navbar import navbar
import dash

# Register the homepage with Dash
dash.register_page(__name__, path='/')

def layout():
    """
    Define the layout for the homepage.

    Returns:
        dbc.Container: A Dash Bootstrap Container component containing the homepage layout.
    """
    return create_homepage_layout()

def create_homepage_layout():
    """
    Create the main layout structure for the homepage.

    Returns:
        dbc.Container: A Dash Bootstrap Container component with the structured content for the homepage.
    """
    
    return dbc.Container(
        [
            # Location component to manage page routing
            dcc.Location(id='_pages_location', refresh=False),
            
            dbc.Row(  # Wrap the columns in a row to align them side by side
                [
                    # Left navbar column
                    dbc.Col(navbar, width=2, style={"padding": 0}),
                    
                    # Main content column
                    dbc.Col(
                        [
                            # Main title row
                            dbc.Row(
                                dbc.Col(
                                    html.H1(
                                        "📊 Financial Sentiment in Focus: A Dashboard for Corporate News Analysis",
                                        style={
                                            'text-align': 'center',
                                            'color': '#2E86C1',
                                            'font-size': '3rem',
                                            'font-weight': 'bold',
                                            'margin-top': '20px',
                                        }
                                    )
                                ),
                                justify="center",
                            ),
                            # Welcome message row
                            dbc.Row(
                                dbc.Col(
                                    html.P(
                                        "Welcome to the Corporate News Analysis Dashboard, where you can explore trends, sentiment, and key insights across news from 11 major companies. 🚀",
                                        style={
                                            'text-align': 'center',
                                            'color': '#1F618D',
                                            'font-size': '1.2rem',
                                            'margin-top': '15px',
                                        }
                                    )
                                ),
                                justify="center",
                            ),
                            html.Hr(),  # Horizontal line for separation
                            
                            # Project overview section
                            dbc.Row(
                                dbc.Col(
                                    html.H3(
                                        "🖥️ Project Overview",
                                        style={
                                            'color': '#2874A6',
                                            'font-weight': 'bold',
                                            'margin-top': '20px',
                                            'text-align': 'left',
                                        }
                                    )
                                ),
                            ),
                            dbc.Row(
                                dbc.Col(
                                    html.P(
                                        "This dashboard provides a comprehensive view of corporate news, allowing you to analyze sentiments, trends, and emotional tones in articles. By leveraging data visualization, you can uncover insights that correlate media narratives with market behavior. 📈",
                                        style={
                                            'color': '#154360',
                                            'font-size': '1.1rem',
                                            'text-align': 'justify',
                                            'margin-bottom': '15px',
                                        }
                                    )
                                ),
                            ),
                            html.Hr(),  # Horizontal line for separation
                            
                            # Explore the dashboard section
                            dbc.Row(
                                dbc.Col(
                                    html.H3(
                                        "🗂️ Explore the Dashboard",
                                        style={
                                            'color': '#2874A6',
                                            'font-weight': 'bold',
                                            'margin-top': '20px',
                                            'text-align': 'left',
                                        }
                                    )
                                ),
                            ),
                            dbc.Row(
                                dbc.Col(
                                    html.Ul(
                                        [
                                            # List of features with descriptions
                                            html.Li(
                                                [
                                                    html.Span(
                                                        "📅 Home: ",
                                                        style={'font-weight': 'bold', 'color': '#1ABC9C'}
                                                    ),
                                                    html.Span(
                                                        "This is the introduction page where you can learn about the project and navigate the dashboard."
                                                    )
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.Span(
                                                        "📰 Article Analysis: ",
                                                        style={'font-weight': 'bold', 'color': '#3498DB'}
                                                    ),
                                                    html.Span(
                                                        "Dive into specific articles, view summaries, and analyze the sentiment and emotional tone through various visualizations."
                                                    )
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.Span(
                                                        "📈 Data Trends & Patterns: ",
                                                        style={'font-weight': 'bold', 'color': '#E74C3C'}
                                                    ),
                                                    html.Span(
                                                        "Explore sentiment and emotional analysis across the entire dataset or subsets, visualizing trends over time."
                                                    )
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.Span(
                                                        "💹 Financial Narrative Insights: ",
                                                        style={'font-weight': 'bold', 'color': '#9B59B6'}
                                                    ),
                                                    html.Span(
                                                        "Compare articles with stock movements, uncovering the influence of media narratives on market performance."
                                                    )
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.Span(
                                                        "📚 About: ",
                                                        style={'font-weight': 'bold', 'color': '#8E44AD'}
                                                    ),
                                                    html.Span(
                                                        "Learn more about the project, its goals, the technology behind it, and the people involved."
                                                    )
                                                ]
                                            )
                                        ],
                                        style={
                                            'list-style-type': 'none',
                                            'font-size': '1.05rem',
                                            'color': '#2C3E50',
                                            'text-align': 'justify',
                                        }
                                    )
                                ),
                            ),
                            html.Hr(),  # Horizontal line for separation
                            
                            # Closing message encouraging exploration
                            dbc.Row(
                                dbc.Col(
                                    html.P(
                                        "Use the navigation bar on the left to explore the different sections and start analyzing the data! 📂",
                                        style={
                                            'text-align': 'center',
                                            'color': '#1F618D',
                                            'font-size': '1.2rem',
                                            'margin-top': '20px',
                                            'margin-bottom': '30px',
                                        }
                                    )
                                ),
                                justify="center",
                            ),
                        ],
                        width=10  # Set the main content column width
                    )
                ],
            )
        ],
        fluid=True,  # Make the container fluid
        style={'padding': '20px'}  # Padding around the container
    )
