import unittest
from TextProcessor import TextProcessor

class TestTextProcessor(unittest.TestCase):

    def setUp(self):
        self.text_processor = TextProcessor()

    def test_remove_special_characters(self):
        input_text = "Hello, this is a test! #python"
        expected_output = "Hello this is a test python"
        self.assertEqual(TextProcessor.remove_special_characters(input_text), expected_output)

    def test_remove_stopwords(self):
        input_text = "This is a test sentence"
        expected_output = "test sentence"
        self.assertEqual(TextProcessor.remove_stopwords(input_text), expected_output)

    def test_remove_urls(self):
        input_text = "Check out this link: https://example.com"
        expected_output = "Check out this link: "
        self.assertEqual(TextProcessor.remove_urls(input_text), expected_output)

    def test_lemmatize_text(self):
        input_text = "dogs running in the park"
        expected_output = "dog running in the park"
        self.assertEqual(TextProcessor.lemmatize_text(input_text), expected_output)

    def test_remove_extra_spaces(self):
        input_text = "   This   is   a   test   "
        expected_output = "This is a test"
        self.assertEqual(TextProcessor.remove_extra_spaces(input_text), expected_output)

    def test_process_text(self):
        input_text = "Check out this link: https://example.com!!!"
        expected_output = "check link"
        self.assertEqual(TextProcessor.process_text(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()
