from configurations.config import my_color_discrete_sequence
from dash import dcc
import plotly.express as px

# Function for generating stacked article count plot
def generate_article_count_plot(df):
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    article_counts = df.groupby(['Month', 'Company']).size().reset_index(name='Count')
    article_counts = article_counts.sort_values(by='Count', ascending=False)

    fig = px.bar(
        article_counts,
        x='Month',
        y='Count',
        color='Company',
        labels={'Month': 'Month', 'Count': 'Count'},
        title='Article Count by Month',
        barmode='stack',
        height=600,
        color_discrete_sequence=my_color_discrete_sequence
    )
    
    return dcc.Graph(figure=fig)

