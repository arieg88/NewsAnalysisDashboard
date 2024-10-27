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
sen_and_tren_icon = './assets/chart-histogram.png'
article_icon = './assets/document.png'

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
    ],
    "trends_and_patterns_page": [
    {"label": "Article Count By Month", "value": "article_count_by_month"},
    {"label": "Article Count By Week", "value": "article_count_by_week"},
    {"label": "Top Entities By Month", "value": "top_entities_by_month"},
    {"label": "Top Entity Types By Month", "value": "top_entity_types_by_month"},
    {"label": "Sentiment Distribution By Company", "value": "sentiment_distribution_by_company"},
    {"label": "Monthly Average Emotion: Joy", "value": "plot_monthly_avg_emotion_joy"},
    # {"label": "Sentiment Analysis by Company", "value": "sentiment_by_company"},
    # {"label": "Monthly Sentiment Score Trends", "value": "monthly_sentiment_trends"},
    # {"label": "Sentiment Analysis by Author", "value": "sentiment_by_author"},
    # {"label": "Sentiment Analysis of Headlines", "value": "headline_sentiment"},
    # {"label": "Cumulative Sentiment Score Over Time", "value": "cumulative_sentiment"},
    # {"label": "Comparison of Stock Performance vs. Sentiment", "value": "stock_vs_sentiment"},
    # {"label": "Sentiment Analysis by Publication Source", "value": "sentiment_by_source"},
    # {"label": "Daily Sentiment Score Variation", "value": "daily_sentiment_variation"},
    # {"label": "Impact of News on Stock Market Trends", "value": "news_stock_impact"},
    # {"label": "Sentiment Analysis of Market Predictions", "value": "market_predictions_sentiment"},
    # {"label": "Sentiment Impact of Earnings Reports", "value": "earnings_report_impact"},
    # {"label": "Sentiment Analysis of International News", "value": "international_news_sentiment"},
    # {"label": "Impact of Political News on Company Sentiment", "value": "political_news_impact"},
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