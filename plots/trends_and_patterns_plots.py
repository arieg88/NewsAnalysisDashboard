# Import necessary libraries and components
from configurations.config import *
from dash import dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go

def plot_stacked_article_count_by_month(df):
    """
    Creates a stacked bar chart of article counts grouped by month and company.
    
    Parameters:
    - df: DataFrame containing 'Month' and 'Company' columns.
    
    Returns:
    - dcc.Graph: Dash Core Components Graph containing the bar chart figure.
    """
    # Group by month and company, then count articles
    article_counts = df.groupby(['Month', 'Company']).size().reset_index(name='Article Count')

    # Sort data within each month by article count (descending)
    article_counts = article_counts.sort_values(by=['Month', 'Article Count'], ascending=[True, False])

    # Create the Plotly figure
    fig = px.bar(
        article_counts,
        x='Month',
        y='Article Count',
        color='Company',
        title='Monthly Article Count by Company',
        labels={'Month': 'Month', 'Article Count': 'Article Count'},
        barmode='stack',
        color_discrete_sequence=my_color_discrete_sequence
    )

    fig.update_layout(
        xaxis_tickformat='%Y-%m',  # Format x-axis as Year-Month
        xaxis_title='Month',
        yaxis_title='Article Count',
        legend_title='Company',
        margin=dict(l=40, r=10, t=40, b=40)
    )

    # Rotate x-axis labels to 45 degrees
    fig.update_xaxes(tickangle=45)
    
    return dcc.Graph(figure=fig)

def plot_stacked_article_count_by_week(df):
    """
    Creates a stacked bar chart of article counts grouped by week and company.
    
    Parameters:
    - df: DataFrame containing 'Week' and 'Company' columns.
    
    Returns:
    - dcc.Graph: Dash Core Components Graph containing the bar chart figure.
    """
    # Group by week and company, then count articles
    article_counts = df.groupby(['Week', 'Company']).size().reset_index(name='Article Count')

    # Sort data within each week by article count (descending)
    article_counts = article_counts.sort_values(by=['Week', 'Article Count'], ascending=[True, False])

    # Create the Plotly figure
    fig = px.bar(
        article_counts,
        x='Week',
        y='Article Count',
        color='Company',
        title='Weekly Article Count by Company',
        labels={'Week': 'Week', 'Article Count': 'Article Count'},
        barmode='stack',
        color_discrete_sequence=my_color_discrete_sequence
    )

    fig.update_layout(
        xaxis_tickformat='%Y-%m',  # Format x-axis as Year-Month
        xaxis_title='Week',
        yaxis_title='Article Count',
        legend_title='Company',
        margin=dict(l=40, r=10, t=40, b=40)
    )

    # Rotate x-axis labels to 45 degrees
    fig.update_xaxes(tickangle=45)

    return dcc.Graph(figure=fig)

def plot_top_entities_by_month(entities_df, final_df):
    """
    Creates a stacked bar chart of the top 10 frequent entities grouped by month.
    
    Parameters:
    - entities_df: DataFrame containing entity data.
    - final_df: DataFrame containing the 'Month' column for merging.
    
    Returns:
    - dcc.Graph: Dash Core Components Graph containing the bar chart figure.
    """
    # Merge entities_df with final_df to add the 'Month' column based on 'Original_index'
    entities_with_month = entities_df.merge(final_df[['Month']], left_on='Original_index', right_index=True)

    # Group by month and entity, count occurrences, and sort within each month
    entity_counts = (
        entities_with_month.groupby(['Month', 'Entity_name']).size()
        .reset_index(name='Count')
        .sort_values(['Month', 'Count'], ascending=[True, False])
    )

    # Select top 10 entities for each month
    entity_counts['Rank'] = entity_counts.groupby('Month')['Count'].rank(method='first', ascending=False)
    top_entities = entity_counts[entity_counts['Rank'] <= 10]

    # Create the stacked bar chart
    fig = px.bar(
        top_entities,
        x='Month',
        y='Count',
        color='Entity_name',
        title='Top 10 Frequent Entities by Month',
        labels={'Month': 'Month', 'Count': 'Entity Count'},
        barmode='stack',
        color_discrete_sequence=my_color_discrete_sequence
    )

    fig.update_layout(
        xaxis_tickformat='%Y-%m',  # Format x-axis as Year-Month
        xaxis_title='Month',
        yaxis_title='Entity Count',
        legend_title='Entity',
        margin=dict(l=40, r=10, t=40, b=40)
    )

    fig.update_xaxes(tickangle=45)  # Rotate x-axis labels
    return dcc.Graph(figure=fig)

def plot_top_entity_types_by_month(entities_df, final_df):
    """
    Creates a stacked bar chart of the top frequent entity types grouped by month.
    
    Parameters:
    - entities_df: DataFrame containing entity data.
    - final_df: DataFrame containing the 'Month' column for merging.
    
    Returns:
    - dcc.Graph: Dash Core Components Graph containing the bar chart figure.
    """
    # Merge entities_df with final_df to add the 'Month' column based on 'Original_index'
    entities_with_month = entities_df.merge(final_df[['Month']], left_on='Original_index', right_index=True)

    # Group by month and entity type, count occurrences, and sort within each month
    type_counts = (
        entities_with_month.groupby(['Month', 'Entity_type']).size()
        .reset_index(name='Count')
        .sort_values(['Month', 'Count'], ascending=[True, False])
    )

    # Select top frequent entity types for each month
    type_counts['Rank'] = type_counts.groupby('Month')['Count'].rank(method='first', ascending=False)
    top_entity_types = type_counts[type_counts['Rank'] <= 10]

    # Create the stacked bar chart
    fig = px.bar(
        top_entity_types,
        x='Month',
        y='Count',
        color='Entity_type',
        title='Top Frequent Entity Types by Month',
        labels={'Month': 'Month', 'Count': 'Entity Type Count'},
        barmode='stack',
        color_discrete_sequence=my_color_discrete_sequence
    )

    fig.update_layout(
        xaxis_tickformat='%Y-%m',  # Format x-axis as Year-Month
        xaxis_title='Month',
        yaxis_title='Entity Type Count',
        legend_title='Entity Type',
        margin=dict(l=40, r=10, t=40, b=40)
    )

    fig.update_xaxes(tickangle=45)  # Rotate x-axis labels

    return dcc.Graph(figure=fig)

def plot_sentiment_distribution_by_company(df):
    """
    Creates a box plot of sentiment scores (FinBERT aggregate) by company.
    
    Parameters:
    - df: DataFrame containing columns 'Company' and 'Agg_Finbert_aggregated_score'
    
    Returns:
    - dcc.Graph: Dash Core Components Graph containing the box plot figure.
    """
    fig = px.box(
        df,
        x='Company',
        y='Agg_Finbert_aggregated_score',
        title='Sentiment Score Distribution by Company',
        labels={'Agg_Finbert_aggregated_score': 'Sentiment Score'},
        color='Company',
        color_discrete_sequence=my_color_discrete_sequence
    )
    
    fig.update_layout(
        xaxis_title='Company',
        yaxis_title='Sentiment Score',
        margin=dict(l=40, r=10, t=40, b=40)
    )
    
    return dcc.Graph(figure=fig)

def plot_monthly_avg_emotion(df, emotion_column):
    """
    Creates a line plot with dots for the monthly average of a specified emotion, with a separate line for each company.
    
    Parameters:
    - df: DataFrame containing 'Month', 'Company', and specified emotion column
    - emotion_column: str, the name of the emotion column to plot (e.g., 'Emotion_Mean_joy')
    
    Returns:
    - dcc.Graph: Dash Core Components Graph containing the line plot figure
    """
    # Calculate the monthly average emotion by company
    monthly_emotion_avg = df.groupby(['Month', 'Company'])[emotion_column].mean().reset_index()
    
    # Create the Plotly figure
    fig = px.line(
        monthly_emotion_avg,
        x='Month',
        y=emotion_column,
        color='Company',
        title=f"Monthly Average of {emotion_column.replace('Emotion_', '').capitalize()}",
        labels={'Month': 'Month', emotion_column: 'Average Score'},
        markers=True,
        color_discrete_sequence=my_color_discrete_sequence
    )

    fig.update_layout(
        xaxis_tickformat='%Y-%m',
        xaxis_title="Month",
        yaxis_title="Average Emotion Score",
        margin=dict(l=40, r=10, t=40, b=40)
    )

    return dcc.Graph(figure=fig)