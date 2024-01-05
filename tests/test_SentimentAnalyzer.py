import unittest
from unittest.mock import MagicMock
from SentimentAnalyzer import SentimentAnalyzer

class TestSentimentAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = SentimentAnalyzer.initialize_sentiment_analyzer()

    def test_initialize_sentiment_analyzer(self):
        # Arrange

        # Act
        analyzer = SentimentAnalyzer.initialize_sentiment_analyzer()

        # Assert
        self.assertIsNotNone(analyzer)

    def test_classify_sentiments(self):
        # Arrange
        lines = ["This is a positive statement.", "This is a neutral statement.", "This is a negative statement."]
        mock_analyzer = MagicMock()
        mock_analyzer.polarity_scores.side_effect = [
            {'compound': 0.8},
            {'compound': 0.04},
            {'compound': -0.7}
        ]

        # Act
        positive, neutral, negative, _, _, _ = SentimentAnalyzer.classify_sentiments(mock_analyzer, lines)

        # Assert
        self.assertEqual(positive, 1)
        self.assertEqual(neutral, 1)
        self.assertEqual(negative, 1)

    def test_calculate_average_sentiment(self):
        # Arrange
        positive_posts, neutral_posts, negative_posts, total_posts = 2, 3, 1, 6

        # Act
        avg_sentiment, overall_sentiment = SentimentAnalyzer.calculate_average_sentiment(
            positive_posts, negative_posts, total_posts
        )

        # Assert
        self.assertEqual(avg_sentiment, 0.17)
        self.assertEqual(overall_sentiment, "Positive")

    def test_calculate_sentiment_direction(self):
        # Arrange
        percent_of_pos, percent_of_neu, percent_of_neg = 40, 30, 30

        # Act
        direction = SentimentAnalyzer.calculate_sentiment_direction(
            percent_of_pos, percent_of_neu, percent_of_neg
        )

        # Assert
        self.assertEqual(direction, "up")

    def test_calculate_overall_sentiment(self):
        # Arrange
        avg_sentiment_positive = 0.2
        avg_sentiment_negative = -0.3
        avg_sentiment_neutral = 0.0

        # Act
        overall_sentiment_positive = SentimentAnalyzer.classify_overall_sentiment(avg_sentiment_positive)
        overall_sentiment_negative = SentimentAnalyzer.classify_overall_sentiment(avg_sentiment_negative)
        overall_sentiment_neutral = SentimentAnalyzer.classify_overall_sentiment(avg_sentiment_neutral)

        # Assert
        self.assertEqual(overall_sentiment_positive, "Positive")
        self.assertEqual(overall_sentiment_negative, "Negative")
        self.assertEqual(overall_sentiment_neutral, "Neutral")

if __name__ == '__main__':
    unittest.main()

