from dash import html
import dash_bootstrap_components as dbc
from components.navbar import navbar
import dash

dash.register_page(__name__, path='/')

def layout():
    return create_homepage_layout()

def create_homepage_layout():
    return dbc.Container(
        [
            dbc.Row(  # Wrap the columns in a row to align them side by side
                [
                    # Left navbar column
                    dbc.Col(navbar, width=2, style={"padding": 0}),
                    
                    # Main content column
                    dbc.Col(
                        [
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
                            html.Hr(),
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
                                        "This dashboard offers a comprehensive view of financial news, analyzing not only sentiment but also emotions, trends, and company-specific insights. With data-driven tools, it helps you visualize market sentiment and identify patterns in corporate news. 📈",
                                        style={
                                            'color': '#154360',
                                            'font-size': '1.1rem',
                                            'text-align': 'justify',
                                            'margin-bottom': '15px',
                                        }
                                    )
                                ),
                            ),
                            html.Hr(),
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
                                                        "📊 Sentiment & Trends: ",
                                                        style={'font-weight': 'bold', 'color': '#3498DB'}
                                                    ),
                                                    html.Span(
                                                        "Explore the overall sentiment and trends in news articles across multiple companies, visualized with dynamic charts and plots."
                                                    )
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.Span(
                                                        "😊 Emotion Analysis: ",
                                                        style={'font-weight': 'bold', 'color': '#E74C3C'}
                                                    ),
                                                    html.Span(
                                                        "Analyze the emotional tone of news content, ranging from joy and trust to fear and anger."
                                                    )
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.Span(
                                                        "📰 Article Insights: ",
                                                        style={'font-weight': 'bold', 'color': '#9B59B6'}
                                                    ),
                                                    html.Span(
                                                        "Dive into specific articles, view summaries, and entity recognition details for a deeper understanding."
                                                    )
                                                ]
                                            ),
                                            html.Li(
                                                [
                                                    html.Span(
                                                        "📉 Comparative Analysis: ",
                                                        style={'font-weight': 'bold', 'color': '#F39C12'}
                                                    ),
                                                    html.Span(
                                                        "Compare sentiment, trends, and patterns across multiple companies over time to track performance and media impact."
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
                            html.Hr(),
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
        fluid=True,
        style={'padding': '20px'}
    )
