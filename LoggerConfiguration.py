import os
import logging
from logging.handlers import RotatingFileHandler

class LoggerConfigurator:
    def __init__(self, logger_name, log_file_path, log_level=logging.DEBUG, max_bytes=250000, backup_count=1):
        self.logger_name = logger_name
        self.log_file_path = log_file_path
        self.log_level = log_level
        self.max_bytes = max_bytes
        self.backup_count = backup_count

    def configure_logger(self):
        logger = logging.getLogger(self.logger_name)
        logger.setLevel(self.log_level)

        log_dir = os.path.dirname(self.log_file_path)
        os.makedirs(log_dir, exist_ok=True)

        handler = RotatingFileHandler(
            filename=self.log_file_path,
            maxBytes=self.max_bytes,
            backupCount=self.backup_count
        )
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        return logger