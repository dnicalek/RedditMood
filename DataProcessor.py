import os
import logging
from datetime import datetime
from TextProcessor import TextProcessor
from CryptoData import CryptoData
from FirebaseManager import FirebaseManager
from SentimentAnalyzer import SentimentAnalyzer
from FileAndFoldersProcessor import FileAndFoldersProcessor
from TimeProcessor import TimeProcessor
from NotificationSender import NotificationSender
from LoggerConfiguration import LoggerConfigurator

class DataProcessor:
    logger_configurator = LoggerConfigurator('DataProcessor', 'logs/DataProcessor.log')
    logger = logger_configurator.configure_logger()

    @staticmethod
    def initialize_data_structures(cryptos):
        num_posts_prev_day = {crypto: 0 for crypto in cryptos}
        num_posts_weeks = {crypto: [0] for crypto in cryptos}
        DataProcessor.logger.info("Initialized data structures.")
        return num_posts_prev_day, num_posts_weeks

    @staticmethod
    def setup_crypto_processing(trade_mood_path, crypto):
        crypto_symbol = CryptoData.get_crypto_symbol(crypto)
        photo_url = CryptoData.get_photo_url(crypto)
        current_timestamp = TimeProcessor.get_current_timestamp()
        crypto_folder = os.path.join(trade_mood_path, crypto)
        result_folder = os.path.join("results", f"{crypto}_res")
        DataProcessor.logger.info("Obtained relevant data and created appropriate folders.")
        return crypto_symbol, photo_url, current_timestamp, crypto_folder, result_folder

    @staticmethod
    def create_data_dict(crypto, crypto_symbol, percent_of_pos, percent_of_neu, percent_of_neg, activity_daily, activity_weekly, num_posts, avg_sentiment, overall_sentiment, sentiment_direction, photo_url, current_timestamp):
        return {
            "crypto": crypto,
            "cryptoSymbol": crypto_symbol,
            "sentimentPositive": percent_of_pos,
            "sentimentNeutral": percent_of_neu,
            "sentimentNegative": percent_of_neg,
            "activityDaily": activity_daily,
            "activityWeekly": activity_weekly,
            "numberOfPosts": num_posts,
            "averageSentiment": avg_sentiment,
            "overallSentiment": overall_sentiment,
            "sentimentDirection": sentiment_direction,
            "photoUrl": photo_url,
            "datetime": current_timestamp
        }

    @staticmethod
    def calculate_activity_daily(crypto, num_posts, num_posts_prev_day, lines):
        try:
            if num_posts_prev_day[crypto] > 0:
                activity_daily = ((num_posts - num_posts_prev_day[crypto]) / num_posts_prev_day[crypto]) * 100
            else:
                activity_daily = 0

            DataProcessor.logger.info("Calculated daily activity: %s", round(activity_daily, 2))
            return round(activity_daily, 2)
        except ZeroDivisionError:
            DataProcessor.logger.exception("Division by 0.")
            return 0

    @staticmethod
    def update_num_posts_weekly(file_number, crypto, num_posts, num_posts_weeks):
        try:
            current_week = (file_number - 1) // 7
            if len(num_posts_weeks[crypto]) <= current_week:
                num_posts_weeks[crypto].append(0)

            num_posts_weeks[crypto][current_week] += num_posts

            return num_posts_weeks
        except Exception as e:
            DataProcessor.logger.exception("Error updating number of posts weekly. %s", str(e))
            return num_posts_weeks

    @staticmethod
    def calculate_activity_variability(crypto, num_posts_weeks):
        try:
            weekly_activity = num_posts_weeks[crypto]
            if len(weekly_activity) >= 2:
                variability = ((weekly_activity[-1] - weekly_activity[-2]) / weekly_activity[-2]) * 100
                DataProcessor.logger.info("Calculated weekly activity: %s", round(variability, 2))
                return round(variability, 2)
            else:
                return 0
        except ZeroDivisionError:
            DataProcessor.logger.exception("Division by 0")
            return 0

    @staticmethod
    def process_crypto_files(trade_mood_path, cryptos, analyzer, db, collection_name, fcm_tokens):
        num_posts_prev_day, num_posts_weeks = DataProcessor.initialize_data_structures(cryptos)
        max_files = max(
            FileAndFoldersProcessor.count_files_in_folder(os.path.join(trade_mood_path, crypto)) for crypto in cryptos)

        for file_number in range(1, max_files + 1):
            for crypto in cryptos:
                crypto_symbol, photo_url, current_timestamp, crypto_folder, result_folder = DataProcessor.setup_crypto_processing(trade_mood_path, crypto)

                try:
                    os.makedirs(result_folder, exist_ok=True)

                    input_file = os.path.join(crypto_folder, f"{crypto}_{file_number}.txt")
                    output_file = os.path.join(result_folder, f"{crypto}_{file_number}_res.json")
                    lines, num_posts = FileAndFoldersProcessor.read_lines_from_file(input_file)
                    total_posts = num_posts
                    if os.path.getsize(input_file) == 0 and total_posts == 0:
                        activity_daily = DataProcessor.calculate_activity_daily(crypto, num_posts, num_posts_prev_day, lines)
                        num_posts_weeks = DataProcessor.update_num_posts_weekly(file_number, crypto, num_posts,
                                                                                num_posts_weeks)
                        activity_weekly = DataProcessor.calculate_activity_variability(crypto, num_posts_weeks)
                        percent_of_pos, percent_of_neu, percent_of_neg = 0.0, 100.0, 0.0
                        avg_sentiment, overall_sentiment, sentiment_direction = 0.0, "Neutral", "steady"
                    else:

                        activity_daily = DataProcessor.calculate_activity_daily(crypto, num_posts, num_posts_prev_day, lines)
                        positive_posts, neutral_posts, negative_posts, percent_of_pos, percent_of_neu, percent_of_neg = analyzer.classify_sentiments(lines)
                        avg_sentiment, overall_sentiment = analyzer.calculate_average_sentiment(positive_posts, negative_posts, total_posts)
                        sentiment_direction = analyzer.calculate_sentiment_direction(percent_of_pos, percent_of_neu, percent_of_neg)
                        num_posts_weeks = DataProcessor.update_num_posts_weekly(file_number, crypto, num_posts, num_posts_weeks)
                        activity_weekly = DataProcessor.calculate_activity_variability(crypto, num_posts_weeks)

                    data = DataProcessor.create_data_dict(crypto, crypto_symbol, percent_of_pos, percent_of_neu, percent_of_neg, activity_daily, activity_weekly, num_posts, avg_sentiment, overall_sentiment, sentiment_direction, photo_url, current_timestamp)
                    FileAndFoldersProcessor.save_data_to_json(output_file, data)
                    FirebaseManager.set_data_firestore(db, collection_name, crypto, data)

                    num_posts_prev_day[crypto] = num_posts

                except FileNotFoundError:
                    DataProcessor.logger.warning(f"File not found: {input_file}")
                except Exception as e:
                    DataProcessor.logger.exception(f"Error processing file {input_file}: {str(e)}")

        #NotificationSender.validate_fcm_tokens(fcm_tokens)
        #NotificationSender.send_notification_to_devices(fcm_tokens)