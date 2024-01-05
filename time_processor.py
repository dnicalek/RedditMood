from datetime import datetime
import time
from logger_configuration import LoggerConfigurator

class TimeProcessor:
    logger_configurator = LoggerConfigurator('TimeProcessor', 'logs/TimeProcessor.log')
    logger = logger_configurator.configure_logger()

    @staticmethod
    def get_current_timestamp():
        try:
            current_datetime = datetime.now()
            timestamp = current_datetime.timestamp()
            TimeProcessor.logger.info(f"Current timestamp: {timestamp}")
            return timestamp
        except Exception as e:
            TimeProcessor.logger.exception(f"Error getting the current timestamp: {str(e)}")
            return None

    @staticmethod
    def delay():
        try:
            TimeProcessor.logger.info("The 30 second delay has been activated.")
            time.sleep(30)
        except Exception as e:
            TimeProcessor.logger.exception(f"Error during program sleep: {str(e)}")
            
