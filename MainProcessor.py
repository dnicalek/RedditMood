from TextProcessor import TextProcessor
from CryptoData import CryptoData
from FirebaseManager import FirebaseManager
from SentimentAnalyzer import SentimentAnalyzer
from FileAndFoldersProcessor import FileAndFoldersProcessor
from TimeProcessor import TimeProcessor
from DataProcessor import DataProcessor
from NotificationSender import NotificationSender
from LoggerConfiguration import LoggerConfigurator
from transformers import pipeline, BertTokenizer, BertForSequenceClassification
import sys

class MainProcessor:
    def __init__(self, trade_mood_path, certificate_path, collection_name):
        self.trade_mood_path = trade_mood_path
        self.certificate_path = certificate_path
        self.collection_name = collection_name

    logger_configurator = LoggerConfigurator('MainProcessor', 'logs/MainProcessor.log')
    logger = logger_configurator.configure_logger()

    def run_main(self):
        try:
            FileAndFoldersProcessor.create_results_folder()

            bert_model_path = "nlptown/bert-base-multilingual-uncased-sentiment"
            analyzer = SentimentAnalyzer(bert_model_path)

            FirebaseManager.initialize_connection_firestore(self.certificate_path)
            db = FirebaseManager.initialize_firestore_client()
            fcm_tokens = NotificationSender.get_fcm_tokens(db)
            cryptos = CryptoData.get_crypto_list()
            DataProcessor.process_crypto_files(self.trade_mood_path, cryptos, analyzer, db,
                                               self.collection_name, fcm_tokens)
            FirebaseManager.close_connection()

            MainProcessor.logger.info("Operacja zakończona pomyślnie.")
        except FileNotFoundError as file_not_found_error:
            MainProcessor.logger.exception("File not found: %s", str(file_not_found_error))
        except PermissionError as permission_error:
            MainProcessor.logger.exception("Permission error: %s", str(permission_error))
        except Exception as generic_exception:
            MainProcessor.logger.exception("An error occurred: %s", str(generic_exception))
            MainProcessor.logger.exception(
                f"Error in file {__file__}, line {sys.exc_info()[-1].tb_lineno}: {str(generic_exception)}")


if __name__ == "__main__":
    trade_mood_path = "D:\\PyCharmProjects\\RedditMood\\reddit_data"
    certificate_path = "C:\\Users\\domin\\TradeMood\\trademood-935a3-firebase-adminsdk-4tlgp-11830c8e95.json"
    collection_name = "instruments"

    main_processor = MainProcessor(trade_mood_path, certificate_path, collection_name)
    main_processor.run_main()

