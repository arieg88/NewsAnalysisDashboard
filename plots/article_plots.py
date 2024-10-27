from configurations.config import *
from dash import dcc
import plotly.express as px
import pandas as pd

def plot_emotion_heatmap(emotion_df, original_index):
    # Filter for the selected article
    article_emotions = emotion_df[emotion_df['Original_index'] == original_index]

    # Convert text_sentences to a DataFrame
    emotion_data = article_emotions['text_sentences'].apply(pd.Series)

    # Create a heatmap
    fig = px.imshow(
        emotion_data.T,  # Transpose to have emotions on the y-axis and sentences on the x-axis
        labels=dict(x="Sentence Index", y="Emotion", color="Word Count"),
        title=f'Emotion Heatmap',
    )
    return dcc.Graph(figure=fig)


# Function to plot emotional journey for a selected article
def plot_emotional_journey(emotion_df, original_index):
    # Filter for the selected article based on Original_index
    article_emotions = emotion_df[emotion_df['Original_index'] == original_index]

    # Expand dictionary into separate emotion columns
    emotion_data = article_emotions['text_sentences'].apply(pd.Series)
    emotion_data['Sentence_index'] = article_emotions['Sentence_index']

    # Filter emotions_list to include only the columns present in emotion_data
    available_emotions = [emotion for emotion in emotions_list if emotion in emotion_data.columns]

    # Melt the data for plotting (convert wide data to long data format)
    plot_df = emotion_data.melt(id_vars=['Sentence_index'], value_vars=available_emotions,
                                var_name='Emotion', value_name='Count')

    # Plot the stacked bar chart using Plotly Express
    fig = px.bar(
        plot_df,
        x='Sentence_index',
        y='Count',
        color='Emotion',
        title=f'Emotional Journey',
        labels={'Sentence_index': 'Sentence', 'Count': 'Emotion Words'},
        color_discrete_sequence=my_color_discrete_sequence,
    )
    return dcc.Graph(figure=fig)


def plot_emotion_distribution(final_df, article_id):
    """
    Generates a bar chart showing the total sum of each emotion for the selected article.

    Args:
        final_df (DataFrame): DataFrame containing articles with their emotion scores.
        article_id (int): The index of the article to filter for.

    Returns:
        A dcc.Graph component containing the Plotly bar chart.
    """

    # Filter the article's emotion data
    filtered_article = final_df[final_df['id'] == article_id]  # Adjust the column name as necessary

    if filtered_article.empty:
        return "No data found for the selected article."

    # Assume emotion columns are named as: 'Emotion_Sum_joy', 'Emotion_Sum_sadness', etc.
    emotion_columns = [col for col in final_df.columns if col.startswith('Emotion_Sum_')]

    # Calculate the sum of each emotion for the selected article
    emotion_sums = {col: filtered_article[col].sum() for col in emotion_columns}

    # Create a DataFrame for plotting
    emotion_sum_df = pd.DataFrame(list(emotion_sums.items()), columns=['Emotion', 'Total Score'])

    # Create the bar chart
    fig = px.bar(
        emotion_sum_df,
        x='Emotion',
        y='Total Score',
        title='Total Emotion Scores for Selected Article',
        text='Total Score',
        labels={'Total Score': 'Emotion Score'},
        color_discrete_sequence=my_color_discrete_sequence,
    )

    fig.update_layout(
        xaxis_title='Emotion',
        yaxis_title='Total Score',
        margin=dict(l=0, r=0, t=60, b=0)
    )

    # Return the Plotly figure wrapped in a dcc.Graph
    return dcc.Graph(figure=fig)


def plot_entity_types_breakdown(entities_df, article_id):
    """
    Generates a pie chart showing the breakdown of entity types found in an article.

    Args:
        entities_df (DataFrame): DataFrame containing entities for all articles.
        article_id (int): The index of the article to filter entities for.

    Returns:
        A dcc.Graph component containing the Plotly pie chart.
    """
    # Filter entities for the selected article
    filtered_entities = entities_df[entities_df['Original_index'] == article_id]
    
    if filtered_entities.empty:
        return "No entities found for the selected article."

    # Count the frequency of each entity type
    entity_type_counts = filtered_entities['Entity_type'].value_counts().reset_index()
    entity_type_counts.columns = ['Entity_type', 'Count']

    # Create the pie chart
    fig = px.pie(
        entity_type_counts,
        values='Count',
        names='Entity_type',
        title='Entity Types Breakdown',
        color='Entity_type',
        color_discrete_sequence=my_color_discrete_sequence
    )

    fig.update_traces(textinfo='percent+label')
    fig.update_layout(
        margin=dict(l=0, r=0, t=60, b=0)
    )

    # Return the Plotly figure wrapped in a dcc.Graph
    return dcc.Graph(figure=fig)

def plot_entities_found_in_article(entities_df, article_id):
    """
    Generates a bar chart showing the frequency of entities found in an article.

    Args:
        entities_df (DataFrame): DataFrame containing entities for all articles.
        article_id (int): The index of the article to filter entities for.

    Returns:
        A Plotly figure of the bar chart.
    """
    # Filter entities for the selected article
    filtered_entities = entities_df[entities_df['Original_index'] == article_id]
    
    if filtered_entities.empty:
        return "No entities found for the selected article."

    # Count the frequency of each entity
    entity_counts = filtered_entities['Entity_name'].value_counts().reset_index()
    entity_counts.columns = ['Entity_name', 'Count']

    # Create the bar chart
    fig = px.bar(
        entity_counts,
        x='Entity_name',
        y='Count',
        title='Entities Found in the Article',
        labels={'Entity_name': 'Entity', 'Count': 'Frequency'},
        color='Count',
        text='Count',
        color_discrete_sequence=my_color_discrete_sequence
    )

    fig.update_traces(texttemplate='%{text}', textposition='outside')
    fig.update_layout(
        xaxis_title="Entities",
        yaxis_title="Frequency",
        showlegend=False,
        margin=dict(l=40, r=40, t=60, b=40),
        xaxis=dict(tickangle=45)  # Rotate x-axis labels by 45 degrees
    )

    return dcc.Graph(figure=fig)


def plot_positive_vs_negative_sentence_count(df, article_id):
    """
    Plot a pie chart of the count of positive vs. negative sentences in a selected article.

    Parameters:
    - df: DataFrame containing the articles with 'Finbert_sentence_list' column.
    - article_index: The index of the article for which to plot the sentiment count.
      The 'Finbert_sentence_list' column should contain a list of dictionaries for each sentence,
      with 'label' (positive, negative, neutral).

    Returns:
    - A Dash component with a pie chart of positive vs. negative sentence count.
    """
    # Extract the list of sentiment dictionaries for the selected article
    sentiment_data = df.loc[article_id, 'Finbert_sentence_list']

    # Filter out neutral sentences and count positive and negative ones
    positive_count = sum(1 for s in sentiment_data if s['label'] == 'Positive')
    negative_count = sum(1 for s in sentiment_data if s['label'] == 'Negative')
    neutral_count = sum(1 for s in sentiment_data if s['label'] == 'Neutral')

    # Prepare data for the pie chart
    labels = ['Positive Sentences', 'Negative Sentences', 'Neutral Sentences']
    values = [positive_count, negative_count, neutral_count]

    # Create the pie chart
    fig = px.pie(
        values=values,
        names=labels,
        title="Positive vs. Negative Sentence Count (FinBERT)",
        color_discrete_sequence=my_color_discrete_sequence
    )

    fig.update_layout(title_x=0.5)

    return dcc.Graph(figure=fig)

def plot_sentiment_analysis_per_sentence(df, article_id):
    """
    Plot Sentiment Analysis per Sentence for a selected article from the DataFrame.
    
    Parameters:
    - df: DataFrame containing the articles. Should include the 'Finbert_sentence_list' column.
    - article_index: The index of the article for which to plot sentiment analysis.
      The 'Finbert_sentence_list' column should contain a list of dictionaries for each sentence,
      with 'label' (positive, negative, neutral) and 'score' (sentiment score).
    
    Returns:
    - A Dash component with a scatter plot of sentiment scores per sentence.
    """
    # Extract the list of sentiment dictionaries for the selected article
    
    sentiment_data = df.loc[article_id, 'Finbert_sentence_list']
    
    # Prepare the data for plotting
    sentence_numbers = list(range(1, len(sentiment_data) + 1))
    sentiment_labels = [s['label'] for s in sentiment_data]

    sentiment_scores = [s['score'] for s in sentiment_data]
    
    # Create a DataFrame for plotting
    plot_df = pd.DataFrame({
        'Sentence Number': sentence_numbers,
        'Sentiment Score': sentiment_scores,
        'Sentiment Label': sentiment_labels
    })
    
    # Create the scatter plot
    fig = px.bar(
        plot_df,
        x='Sentence Number',
        y='Sentiment Score',
        color='Sentiment Label',
        labels={'x': 'Sentence Number', 'y': 'Sentiment Score'},
        title="Sentiment Analysis per Sentence (FinBERT)",
        color_discrete_sequence=my_color_discrete_sequence
    )
    
    fig.update_layout(
        xaxis_title="Sentence Number",
        yaxis_title="Sentiment Score",
        title_x=0.5
    )
    
    return dcc.Graph(figure=fig)


