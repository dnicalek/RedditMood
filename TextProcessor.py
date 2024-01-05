import string
import re
import nltk
from nltk.corpus import stopwords
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
            TextProcessor.logger.info("Removed special characters and punctuation.")
            return ''.join(char for char in text if char not in string.punctuation)
        except Exception as e:
            TextProcessor.logger.exception("Error while removing special characters. %s", str(e))
            return text

    @staticmethod
    def remove_stopwords(text):
        try:
            words = text.split()
            words = [word.lower() for word in words]
            filtered_words = [word for word in words if word not in stopwords.words('english')]
            TextProcessor.logger.info("Removed stop words.")
            return ' '.join(filtered_words)
        except Exception as e:
            TextProcessor.logger.exception("Error while removing stop words. %s", str(e))
            return text

    @staticmethod
    def remove_urls(text):
        try:
            url_pattern = re.compile(r'https?://\S+|www\.\S+')
            TextProcessor.logger.info("Removed URLs.")
            return url_pattern.sub('', text)
        except Exception as e:
            TextProcessor.logger.exception("Error while removing URLs. %s", str(e))
            return text

    @staticmethod
    def lemmatize_text(text):
        try:
            lemmatizer = WordNetLemmatizer()
            words = text.split()
            lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
            TextProcessor.logger.info("Lemmatized text.")
            return ' '.join(lemmatized_words)
        except Exception as e:
            TextProcessor.logger.exception("Error during lemmatization. %s", str(e))
            return text

    @staticmethod
    def remove_extra_spaces(text):
        try:
            TextProcessor.logger.info("Removed extra spaces.")
            return ' '.join(text.split())
        except Exception as e:
            TextProcessor.logger.exception("Error while removing extra spaces. %s", str(e))
            return text

    @staticmethod
    def normalize_case(text):
        try:
            normalized_text = text.lower()
            TextProcessor.logger.info("Normalized text case.")
            return normalized_text
        except Exception as e:
            TextProcessor.logger.exception("Error during case normalization. %s", str(e))
            return text

    @staticmethod
    def remove_numbers(text):
        try:
            text_without_numbers = re.sub(r'\d+', '', text)
            TextProcessor.logger.info("Removed numbers.")
            return text_without_numbers
        except Exception as e:
            TextProcessor.logger.exception("Error while removing numbers. %s", str(e))
            return text

    @staticmethod
    def remove_slang_and_shortcuts(text):

        slang_and_shortcuts = {
                'lol': 'laugh out loud',
                'btw': 'by the way',
                'brb': 'be right back',
                'omg': 'oh my god',
                'imo': 'in my opinion',
                'fyi': 'for your information',
                'tbh': 'to be honest',
                'idk': 'I don\'t know',
                'thx': 'thanks',
                'np': 'no problem',
                'irl': 'in real life',
                'yolo': 'you only live once',
                'imo': 'in my opinion',
                'fomo': 'fear of missing out',
                'bff': 'best friends forever',
                'gtg': 'got to go',
                'smh': 'shaking my head',
                'nsfw': 'not safe for work',
                'tmi': 'too much information',
                'fwiw': 'for what it\'s worth',
                'rofl': 'rolling on the floor laughing',
                'ttyl': 'talk to you later',
                'icymi': 'in case you missed it',
                'j/k': 'just kidding',
                'tl;dr': 'too long; didn\'t read',
                'afaik': 'as far as I know',
                'tbt': 'throwback Thursday',
                'hmu': 'hit me up',
                'fml': 'f*** my life',
                'smh': 'shake my head',
                'nvm': 'never mind',
                'imo': 'in my opinion',
                'irl': 'in real life',
                'otp': 'on the phone',
                'afk': 'away from keyboard',
                'bffl': 'best friends for life',
                'brt': 'be right there',
                'gtfo': 'get the f*** out',
                'hbd': 'happy birthday',
                'lmao': 'laughing my a** off',
                'omw': 'on my way',
                'rsvp': 'please respond',
                'smh': 'shaking my head',
                'tgif': 'thank God it\'s Friday',
                'wtf': 'what the f***',
                'yolo': 'you only live once',
                'y2k': 'year 2000',
        }
        try:
            for shortcut, expansion in slang_and_shortcuts.items():
                text = text.replace(shortcut, expansion)
            TextProcessor.logger.info("Removed slang and shortcuts.")
            return text
        except Exception as e:
            TextProcessor.logger.exception("Error while removing slang and shortcuts. %s", str(e))
            return text

    @staticmethod
    def process_text(text):
        try:
            text = TextProcessor.remove_urls(text)
            text = TextProcessor.lemmatize_text(text)
            text = TextProcessor.remove_extra_spaces(text)
            text = TextProcessor.remove_special_characters(text)
            text = TextProcessor.remove_stopwords(text)
            text = TextProcessor.normalize_case(text)
            text = TextProcessor.remove_numbers(text)
            text = TextProcessor.remove_slang_and_shortcuts(text)
            TextProcessor.logger.info("Processed text.")
            return text
        except Exception as e:
            TextProcessor.logger.exception("Error during text processing. %s", str(e))
            return text
