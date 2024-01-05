import os
import json
import re
from datetime import datetime
from logger_configuration import LoggerConfigurator

class FileAndFoldersProcessor:
    logger_configurator = LoggerConfigurator('FileAndFoldersProcessor', 'logs/FileAndFoldersProcessor.log')
    logger = logger_configurator.configure_logger()

    @staticmethod
    def create_results_folder():
        try:
            results_folder = "results"
            if not os.path.exists(results_folder):
                os.mkdir(results_folder)
                FileAndFoldersProcessor.logger.info("Created folder 'results'.")
        except FileNotFoundError as e:
            FileAndFoldersProcessor.logger.exception("Error creating folder 'results': %s", str(e))
        except Exception as e:
            FileAndFoldersProcessor.logger.exception("Unexpected error creating folder 'results': %s", str(e))

    @staticmethod
    def count_files_in_folder(folder_path):
        try:
            file_count = 0
            for item in os.listdir(folder_path):
                item_path = os.path.join(folder_path, item)
                if os.path.isfile(item_path):
                    file_count += 1
            FileAndFoldersProcessor.logger.info("Counted files in folder: %s", file_count)
            return file_count
        except FileNotFoundError as e:
            FileAndFoldersProcessor.logger.exception("Folder not found: %s", str(e))
            return 0
        except Exception as e:
            FileAndFoldersProcessor.logger.exception("Error counting files in folder: %s", str(e))
            return 0



    # @staticmethod
    # def read_lines_from_file(input_file):
    #     try:
    #         with open(input_file, "r", encoding="utf-8") as f:
    #             lines = f.readlines()
    #             num_posts = len(lines)
    #
    #         FileAndFoldersProcessor.logger.info("Read lines from file. Number of posts: %s", num_posts)
    #         return lines, num_posts
    #     except FileNotFoundError as e:
    #         FileAndFoldersProcessor.logger.exception("File not found: %s", str(e))
    #         return [], 0
    #     except Exception as e:
    #         FileAndFoldersProcessor.logger.exception("Error reading file: %s", str(e))
    #         return [], 0


    @staticmethod
    def read_lines_from_file(input_file):
        try:
            with open(input_file, "r", encoding="utf-8") as f:
                text = f.read()
                lines = re.split(r'\n\s*\n', text)  # Podział na posty po dowolnej liczbie nowych linii
                num_posts = sum(1 for post in lines if post.strip())  # Pominięcie pustych postów

            FileAndFoldersProcessor.logger.info("Read lines from file. Number of posts: %s", num_posts)
            return lines, num_posts
        except FileNotFoundError as e:
            FileAndFoldersProcessor.logger.exception("File not found: %s", str(e))
            return [], 0
        except Exception as e:
            FileAndFoldersProcessor.logger.exception("Error reading file: %s", str(e))
            return [], 0

    @staticmethod
    def save_data_to_json(output_file, data):
        try:
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
                FileAndFoldersProcessor.logger.info("Saved data to JSON file.")
        except Exception as e:
            FileAndFoldersProcessor.logger.exception("Error saving data to JSON file: %s", str(e))
