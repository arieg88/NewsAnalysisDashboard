from dash import html, dcc
import dash_bootstrap_components as dbc
from components.navbar import navbar
import dash

# Register the about page with Dash
dash.register_page(__name__, path='/about')

def layout():
    """
    Define the layout for the about page.

    Returns:
        dbc.Container: A Dash Bootstrap Container component containing the layout for the about page.
    """
    return create_about_layout()

def create_about_layout():
    """
    Create the layout structure for the about page, describing the project in detail.

    Returns:
        dbc.Container: A Dash Bootstrap Container component with the structured content for the about page.
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
                                        "🔍 About the Project",
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
                            html.Hr(),  # Horizontal line for separation
                            
                            # Project introduction section
                            dbc.Row(
                                dbc.Col(
                                    html.P(
                                        "🕵️‍♂️ This project started with gathering article links using a custom-built Google scraper powered by Selenium. To bypass Google’s CAPTCHA barriers, I designed it to strategically collect news links about major companies from Yahoo Finance 📑.",
                                        style={
                                            'color': '#154360',
                                            'font-size': '1.1rem',
                                            'text-align': 'justify',
                                            'margin-top': '15px',
                                            'margin-bottom': '15px',
                                        }
                                    )
                                ),
                            ),
                            dbc.Row(
                                dbc.Col(
                                    html.P(
                                        "📰 With a trove of links in hand, I crafted a Yahoo Finance scraper to retrieve key article details: title, date, author, and full text. These details form the foundation of our analysis.",
                                        style={
                                            'color': '#1F618D',
                                            'font-size': '1.1rem',
                                            'text-align': 'justify',
                                            'margin-bottom': '15px',
                                        }
                                    )
                                ),
                            ),
                            dbc.Row(
                                dbc.Col(
                                    html.P(
                                        "📊 After scraping, I organized the data in Jupyter, creating several DataFrames with sentiment analyses using FinBERT and Vader, emotional tone analysis, entity extraction, and stock data for correlation analysis.",
                                        style={
                                            'color': '#2874A6',
                                            'font-size': '1.1rem',
                                            'text-align': 'justify',
                                            'margin-bottom': '15px',
                                        }
                                    )
                                ),
                            ),
                            dbc.Row(
                                dbc.Col(
                                    html.P(
                                        "🚀 I gathered more than 10K articles for these companies in 2024. For ease of use, this dashboard operates on a sample of the data, keeping it light and optimized for free-tier hosting on Render. Explore the complete project repositories linked below!",
                                        style={
                                            'color': '#154360',
                                            'font-size': '1.1rem',
                                            'text-align': 'justify',
                                            'margin-bottom': '15px',
                                        }
                                    )
                                ),
                            ),
                            
                            # GitHub repository links
                            dbc.Row(
                                dbc.Col(
                                    html.Ul(
                                        [
                                            html.Li(
                                                html.A("📂 Scrapers & Dataset Building GitHub Repo", href="https://github.com/arieg88/FinanceDataBuilder", target="_blank"),
                                                style={'font-size': '1.1rem', 'color': '#1ABC9C'}
                                            ),
                                            html.Li(
                                                html.A("📊 Dashboard GitHub Repo", href="https://github.com/arieg88/NewsAnalysisDashboard/", target="_blank"),
                                                style={'font-size': '1.1rem', 'color': '#3498DB'}
                                            ),
                                        ],
                                        style={
                                            'list-style-type': 'none',
                                            'text-align': 'left',
                                            'margin-top': '10px',
                                            'margin-bottom': '20px',
                                        }
                                    )
                                ),
                            ),
                            html.Hr(),  # Horizontal line for separation
                            
                            # About Me section
                            dbc.Row(
                                dbc.Col(
                                    html.H3(
                                        "👤 About Me",
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
                                        "👋 I'm a data enthusiast with a keen interest in data-driven storytelling. I love working at the intersection of finance and technology, uncovering insights that help understand market behaviors and trends. 🌐 Let’s connect and explore how data shapes the world!",
                                        style={
                                            'color': '#1F618D',
                                            'font-size': '1.1rem',
                                            'text-align': 'justify',
                                            'margin-bottom': '30px',
                                        }
                                    )
                                ),
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
