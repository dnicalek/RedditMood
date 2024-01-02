from datetime import datetime
import time
from LoggerConfiguration import LoggerConfigurator

class TimeProcessor:
    logger_configurator = LoggerConfigurator('TimeProcessor', 'logs/TimeProcessor.log')
    logger = logger_configurator.configure_logger()

    @staticmethod
    def get_current_timestamp():
        try:
            current_datetime = datetime.now()
            timestamp = current_datetime.timestamp()
            TimeProcessor.logger.info(f"Aktualny znacznik czasu: {timestamp}")
            return timestamp
        except Exception as e:
            TimeProcessor.logger.exception(f"Błąd podczas pobierania aktualnego znacznika czasu: {str(e)}")
            return None

    @staticmethod
    def delay():
        try:
            TimeProcessor.logger.info("Opóźnienie na 30 sekund zostało aktywowane.")
            time.sleep(30)
        except Exception as e:
            TimeProcessor.logger.exception(f"Błąd podczas uśpienia programu: {str(e)}")
            
