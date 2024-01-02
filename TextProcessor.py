import string
import nltk
from nltk.corpus import stopwords
import re
from nltk.stem import WordNetLemmatizer
from LoggerConfiguration import LoggerConfigurator

class TextProcessor:
    def __init__(self):
        nltk.download('stopwords')

    logger_configurator = LoggerConfigurator('TextProcessor', 'logs/TextProcessor.log')
    logger = logger_configurator.configure_logger()

    @staticmethod
    def remove_special_characters(text):
        try:
            # Usuwa znaki specjalne i interpunkcyjne
            TextProcessor.logger.info("Usunięto znaki specjalne i interpunkcyjne. ")
            return ''.join(char for char in text if char not in string.punctuation)
        except Exception as e:
            TextProcessor.logger.exception("Błąd podczas usuwania znaków specjalnych. %s", str(e))
            return text

    @staticmethod
    def remove_stopwords(text):
        try:
            words = text.split()
            words = [word.lower() for word in words]
            filtered_words = [word for word in words if word not in stopwords.words('english')]
            TextProcessor.logger.info("Usunięto stop words. ")
            return ' '.join(filtered_words)
        except Exception as e:
            TextProcessor.logger.exception("Błąd podczas usuwania stop words. %s", str(e))
            return text

    @staticmethod
    def remove_urls(text):
        try:
            url_pattern = re.compile(r'https?://\S+|www\.\S+')
            TextProcessor.logger.info("Usunięto adresy URL. ")
            return url_pattern.sub('', text)
        except Exception as e:
            TextProcessor.logger.exception("Błąd podczas usuwania adresów URL. %s", str(e))
            return text

    @staticmethod
    def lemmatize_text(text):
        try:
            lemmatizer = WordNetLemmatizer()
            words = text.split()
            lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
            TextProcessor.logger.info("Dokonano lematyzacji tekstu. ")
            return ' '.join(lemmatized_words)
        except Exception as e:
            TextProcessor.logger.exception("Błąd podczas lematyzacji tekstu. %s", str(e))
            return text

    @staticmethod
    def remove_extra_spaces(text):
        try:
            TextProcessor.logger.info("Usunięto nadmiarowe spacje. ")
            return ' '.join(text.split())
        except Exception as e:
            TextProcessor.logger.exception("Błąd podczas usuwania nadmiarowych spacji. %s", str(e))
            return text

    @staticmethod
    def process_text(text):
        try:
            text = TextProcessor.remove_urls(text)
            text = TextProcessor.lemmatize_text(text)
            text = TextProcessor.remove_extra_spaces(text)
            text = TextProcessor.remove_special_characters(text)
            text = TextProcessor.remove_stopwords(text)
            TextProcessor.logger.info("Przetworzono tekst. ")
            return text
        except Exception as e:
            TextProcessor.logger.exception("Błąd podczas przetwarzania tekstu. %s", str(e))
            return text
