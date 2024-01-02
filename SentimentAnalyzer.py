from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from TextProcessor import TextProcessor
from LoggerConfiguration import LoggerConfigurator

class SentimentAnalyzer:

    logger_configurator = LoggerConfigurator('SentimentAnalyzer', 'logs/SentimentAnalyzer.log')
    logger = logger_configurator.configure_logger()
    @staticmethod
    def initialize_sentiment_analyzer():
        try:
            SentimentAnalyzer.logger.info("Initializing sentiment analyzer.")
            return SentimentIntensityAnalyzer()
        except Exception as e:
            SentimentAnalyzer.logger.exception(f"Error during sentiment analyzer initialization: {str(e)}")
            return None

    @staticmethod
    def classify_sentiments(analyzer, lines):
        positive_posts, neutral_posts, negative_posts = 0, 0, 0
        positive_threshold, negative_threshold = 0.05, -0.05

        for line in lines:
            try:
                cleaned_line = TextProcessor.process_text(line)
                sentiment = analyzer.polarity_scores(cleaned_line)
                compound_score = sentiment['compound']

                if compound_score >= positive_threshold:
                    positive_posts += 1
                elif compound_score <= negative_threshold:
                    negative_posts += 1
                else:
                    neutral_posts += 1
            except Exception as e:
                SentimentAnalyzer.logger.exception(f"An error occurred during sentiment analysis: {str(e)}")

        total_posts = positive_posts + neutral_posts + negative_posts

        percent_of_pos = SentimentAnalyzer.calculate_percentage(positive_posts, total_posts)
        percent_of_neu = SentimentAnalyzer.calculate_percentage(neutral_posts, total_posts)
        percent_of_neg = SentimentAnalyzer.calculate_percentage(negative_posts, total_posts)

        return positive_posts, neutral_posts, negative_posts, percent_of_pos, percent_of_neu, percent_of_neg

    @staticmethod
    def calculate_average_sentiment(positive_posts, negative_posts, total_posts):
        try:
            if total_posts == 0:
                avg_sentiment = 0
            else:
                avg_sentiment = (positive_posts - negative_posts) / total_posts

            overall_sentiment = SentimentAnalyzer.classify_overall_sentiment(avg_sentiment)

            return round(avg_sentiment, 2), overall_sentiment
        except ZeroDivisionError:
            return 0, "Neutral"

    @staticmethod
    def calculate_sentiment_direction(percent_of_pos, percent_of_neu, percent_of_neg):
        if percent_of_pos > percent_of_neu and percent_of_pos > percent_of_neg:
            return "up"
        elif percent_of_neg > percent_of_neu and percent_of_neg > percent_of_pos:
            return "down"
        else:
            return "steady"

    @staticmethod
    def calculate_percentage(part, whole):
        try:
            return round((part / whole) * 100, 2)
        except ZeroDivisionError:
            return 0

    @staticmethod
    def classify_overall_sentiment(avg_sentiment):
        if avg_sentiment > 0:
            return "Positive"
        elif avg_sentiment < 0:
            return "Negative"
        else:
            return "Neutral"
