import plotly.express as px

article_page_name = 'article_page'
trends_page_name = 'trends_and_patterns_page'

# my_color_discrete_sequence=px.colors.cyclical.IceFire
# my_color_discrete_sequence=px.colors.qualitative.Vivid
my_color_discrete_sequence = px.colors.sequential.Plasma
companies = ['Apple', 'Microsoft', 'Nvidia', 'Amazon', 'Meta', 'Alphabet', 'Berkshire Hathaway', 'Broadcom', 'Eli Lilly', 'Jpmorgan', 'Tesla'] 
emotions_list = ['anticipation', 'fear', 'negative', 'joy', 'positive', 'surprise', 'trust', 'anger', 'disgust', 'sadness']

# Navbar Components
project_logo = "../assets/logo.png"
home_icon = "./assets/home.png"
user_icon = "./assets/user.png"
trend_and_patterns_icon = './assets/magnifying-glass.png'
article_icon = './assets/document.png'
financial_narrative_icon = './assets/chart-histogram.png'

# Define the available options
categories = {
"article_page": [
    {"label": "Sentiment Analysis Per Sentence", "value": "sentiment_analysis_per_sentence"},
    {"label": "Positive vs. Negative Sentence Count", "value": "positive_vs_negative_sentence_count"},
    {"label": "Entities Found in the Article", "value": "entities_found_in_article"},
    {"label": "Entity Types Breakdown", "value": "entity_types_breakdown"},
    {"label": "Emotional Journey", "value": "emotional_journey"},
    {"label": "Emotions Distribution", "value": "emotion_distribution"},
    {"label": "Emotion Heatmap (Across Sentences)", "value": "emotion_heatmap"},
    {"label": "Wordcloud", "value": "wordcloud"},
    {"label": "Comparison of Sentence Sentiment", "value": "comparison_sentence_sentiment"},
    {"label": "Article Emotion Radar", "value": "article_emotion_radar"},
    # {"label": "Top 10 Most Emotional Sentences", "value": "top_emotional_sentences"},  # Highlight the most emotionally charged sentences
    # {"label": "Keyword Frequency Analysis", "value": "keyword_frequency_analysis"},  # Analyze the frequency of key terms
    # {"label": "Summary of Main Topics", "value": "summary_of_main_topics"},  # Provide a summary of key topics discussed
    # {"label": "Comparison of Entities by Sentiment", "value": "entities_by_sentiment"},  # Compare sentiment associated with different entities
    # {"label": "Sentence Length vs. Sentiment", "value": "sentence_length_vs_sentiment"},  # Analyze how sentence length affects sentiment scores
    # {"label": "Pacing of Emotions Throughout the Article", "value": "pacing_of_emotions"},  # Visualize emotional pacing in the article
    # {"label": "Publication Date Impact on Sentiment", "value": "publication_date_impact"},  # Investigate how publication date influences sentiment
    # {"label": "Reader Reactions and Engagement", "value": "reader_reactions_engagement"},  # Analyze audience reactions and engagement metrics
    # {"label": "Thematic Clusters of Sentiment", "value": "thematic_clusters_sentiment"},  # Explore clusters of related themes and their sentiments
    # {"label": "Comparison of Author Sentiment Styles", "value": "author_sentiment_styles"},  # Compare sentiment analysis across different authors
    {"label": "Visualizing the Narrative Arc", "value": "narrative_arc"},  # Create a visual representation of the narrative arc
    # {"label": "Contextual Emotion Analysis", "value": "contextual_emotion_analysis"},  # Analyze emotions in the context of surrounding sentences
    # {"label": "Trend Analysis of Keywords Over Time", "value": "keyword_trend_analysis"},  # Examine how keyword trends change over time
    # {"label": "Interactive Sentiment Explorer", "value": "interactive_sentiment_explorer"},  # Provide an interactive tool to explore sentiment data
],

"trends_and_patterns_page": [
    {"label": "Article Count By Month", "value": "article_count_by_month"},  
    {"label": "Article Count By Week", "value": "article_count_by_week"},  
    {"label": "Top Entities By Month", "value": "top_entities_by_month"},  
    {"label": "Top Entity Types By Month", "value": "top_entity_types_by_month"},  
    {"label": "Sentiment Distribution By Company", "value": "sentiment_distribution_by_company"},  
    {"label": "Monthly Average Emotion: Joy", "value": "plot_monthly_avg_emotion_joy"},  
    # {"label": "Monthly Article Sentiment Trend", "value": "monthly_article_sentiment_trend"},  # New idea
    # {"label": "Common Keywords Over Time", "value": "common_keywords_over_time"},  # New idea
    # {"label": "Article Popularity Trend", "value": "article_popularity_trend"},  # New idea
    # {"label": "Emotion Distribution by Month", "value": "emotion_distribution_by_month"},  # New idea
    # {"label": "Comparative Sentiment Analysis by Company", "value": "comparative_sentiment_analysis"},  # New idea
    # {"label": "Trend of Article Length Over Time", "value": "article_length_trend"},  # New idea
],
    "emotion_page": [
    {"label": "Emotion Scores Distribution", "value": "emotion_distribution"},
    {"label": "Emotion Trends Over Time", "value": "emotion_trends"},
    {"label": "Comparative Emotion Analysis", "value": "compare_emotions"},
    {"label": "Analysis of Common Phrases in Articles", "value": "common_phrases_analysis"},
    {"label": "Comparative Analysis of Emotion Scores", "value": "compare_emotion_scores"},
    {"label": "Variation of Sentiment Scores by Time of Day", "value": "time_of_day_sentiment"},
    {"label": "Distribution of Emotion Scores in Articles", "value": "emotion_distribution"},
    {"label": "Monthly Summary of Emotion Trends", "value": "monthly_emotion_summary"},
    {"label": "Correlation Between Emotion Scores", "value": "emotion_correlation"},
    {"label": "Exploration of Sentence-Level Sentiment", "value": "sentence_sentiment"},
    ],
    "comparative_page": [
        {"label": "Correlation Between Sentiment and Stock Prices", "value": "sentiment_stock_correlation"},
        {"label": "Comparison of BART Summaries", "value": "compare_bart_summaries"},
        {"label": "Comparative Analysis of Top Authors", "value": "compare_top_authors"},
        {"label": "Comparison of Article Length vs. Sentiment", "value": "length_vs_sentiment"},
        {"label": "Comparative Sentiment Analysis Between Companies", "value": "compare_companies"},
        {"label": "Comparative Analysis of Non-Tech vs. Tech Sentiment", "value": "nontech_vs_tech"},
        {"label": "Effect of Seasonal Trends on Sentiment", "value": "seasonal_sentiment_trends"},
        {"label": "Impact of Major News Events on Sentiment", "value": "major_news_impact"},
        {"label": "Comparative Analysis of Emotion Scores", "value": "compare_emotion_scores"},
        {"label": "Impact of Regulation News on Stock Sentiment", "value": "regulation_impact"},
        {"label": "Impact of Celebrity Mentions on Stock Prices", "value": "celebrity_impact"},
        {"label": "Trend Analysis of Tech Company News", "value": "tech_company_trends"},
        {"label": "Exploration of Financial News Sentiment", "value": "financial_news_sentiment"},
        {"label": "Top Emerging Trends in Financial News", "value": "emerging_financial_trends"},
        {"label": "Analysis of Articles by Date Range", "value": "articles_by_date_range"},
    ],
}

page_labels = {
        "trends_and_patterns_page": "Trends And Patterns Analysis",
        "emotion_page": "Emotion Analysis",
        "article_page": "Article Analysis",
        "comparative_page": "Comparative and Correlation Analysis",
    }