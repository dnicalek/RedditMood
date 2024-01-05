import unittest
from unittest.mock import patch
from data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):

    def test_initialize_data_structures(self):
        # Arrange
        cryptos = ["Bitcoin", "Ethereum", "Litecoin"]

        # Act
        result1, result2 = DataProcessor.initialize_data_structures(cryptos)

        # Assert
        self.assertEqual(result1, {"Bitcoin": 0, "Ethereum": 0, "Litecoin": 0})
        self.assertEqual(result2, {"Bitcoin": [0], "Ethereum": [0], "Litecoin": [0]})

    def test_setup_crypto_processing(self):
        def test_setup_crypto_processing(self):
            # Arrange
            trade_mood_path = "/path/to/trade/mood"
            crypto = "Bitcoin"

            # Act
            result1, result2, result3, result4, result5 = DataProcessor.setup_crypto_processing(trade_mood_path, crypto)

            # Assert
            expected_result1 = "BTC"
            expected_result2 = "https://cryptologos.cc/logos/bitcoin-btc-logo.png"
            expected_result3 = isinstance(result3, float)  # Checking if the timestamp is a float
            expected_result4 = "/path/to/trade/mood/Bitcoin"
            expected_result5 = "/path/to/trade/mood/results/Bitcoin_res"

            self.assertEqual(result1, expected_result1)
            self.assertEqual(result2, expected_result2)
            self.assertTrue(expected_result3)
            self.assertEqual(result4, expected_result4)
            self.assertEqual(result5, expected_result5)

    def test_create_data_dict(self):
        # Arrange
        crypto = "Bitcoin"
        crypto_symbol = "BTC"
        percent_of_pos = 50
        percent_of_neu = 30
        percent_of_neg = 20
        activity_daily = 10.5
        activity_weekly = 5.5
        num_posts = 100
        avg_sentiment = 0.75
        overall_sentiment = "Positive"
        sentiment_direction = "up"
        photo_url = "https://cryptologos.cc/logos/bitcoin-btc-logo.png"
        current_timestamp = 1636465640.123456

        # Act
        result = DataProcessor.create_data_dict(crypto, crypto_symbol, percent_of_pos, percent_of_neu, percent_of_neg,
                                                activity_daily, activity_weekly, num_posts, avg_sentiment,
                                                overall_sentiment, sentiment_direction, photo_url, current_timestamp)

        # Assert
        expected_result = {
            "crypto": "Bitcoin",
            "cryptoSymbol": "BTC",
            "sentimentPositive": 50,
            "sentimentNeutral": 30,
            "sentimentNegative": 20,
            "activityDaily": 10.5,
            "activityWeekly": 5.5,
            "numberOfPosts": 100,
            "averageSentiment": 0.75,
            "overallSentiment": "Positive",
            "sentimentDirection": "up",
            "photoUrl": "https://cryptologos.cc/logos/bitcoin-btc-logo.png",
            "datetime": 1636465640.123456
        }

        self.assertEqual(result, expected_result)

    @patch("DataProcessor.SentimentAnalyzer.classify_sentiments")
    def test_calculate_activity_daily(self, mock_classify_sentiments):
        # Arrange
        crypto = "Bitcoin"
        num_posts = 50
        num_posts_prev_day = {"Bitcoin": 30}
        analyzer = mock_classify_sentiments.return_value
        lines = ["Post 1", "Post 2", "Post 3"]

        # Act
        result = DataProcessor.calculate_activity_daily(crypto, num_posts, num_posts_prev_day, analyzer, lines)

        # Assert
        self.assertEqual(result, 66.67)

    def test_calculate_activity_variability(self):
        # Arrange
        crypto = "Bitcoin"
        num_posts_weeks = {"Bitcoin": [30, 40, 50, 60]}

        # Act
        result = DataProcessor.calculate_activity_variability(crypto, num_posts_weeks)

        # Assert
        self.assertEqual(result, 50.0)

    def test_update_num_posts_weekly(self):
        # Arrange
        file_number = 29
        crypto = "Bitcoin"
        num_posts = 20
        num_posts_weeks = {"Bitcoin": [30, 40, 50, 60]}

        # Act
        result = DataProcessor.update_num_posts_weekly(file_number, crypto, num_posts, num_posts_weeks)

        # Assert
        expected_result = {"Bitcoin": [30, 40, 50, 60, 20]}
        self.assertEqual(result, expected_result)

    def test_calculate_activity_variability(self):
        # Arrange
        crypto = "Bitcoin"
        num_posts_weeks = {"Bitcoin": [30, 40, 50, 60]}

        # Act
        result = DataProcessor.calculate_activity_variability(crypto, num_posts_weeks)

        # Assert
        self.assertEqual(result, 20.0)

if __name__ == '__main__':
    unittest.main()
