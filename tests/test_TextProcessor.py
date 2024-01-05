import unittest
from TextProcessor import TextProcessor

class TestTextProcessor(unittest.TestCase):
    def setUp(self):
        self.text_processor = TextProcessor()

    def test_remove_special_characters(self):
        text = "Hello! How are you?"
        processed_text = self.text_processor.remove_special_characters(text)
        self.assertEqual(processed_text, "Hello How are you")

    def test_remove_stopwords(self):
        text = "This is a sample sentence with some stopwords"
        processed_text = self.text_processor.remove_stopwords(text)
        self.assertEqual(processed_text, "sample sentence stopwords")

    def test_remove_urls(self):
        text = "Check out this website: https://www.example.com"
        processed_text = self.text_processor.remove_urls(text)
        self.assertEqual(processed_text, "Check out this website: ")

    def test_lemmatize_text(self):
        text = "running jumping swimming"
        processed_text = self.text_processor.lemmatize_text(text)
        self.assertEqual(processed_text, "running jumping swimming")

    def test_remove_extra_spaces(self):
        text = "  This   is  a  text with   extra   spaces  "
        processed_text = self.text_processor.remove_extra_spaces(text)
        self.assertEqual(processed_text, "This is a text with extra spaces")

    def test_normalize_case(self):
        text = "ThIs Is A sAmPlE TeXt"
        processed_text = self.text_processor.normalize_case(text)
        self.assertEqual(processed_text, "this is a sample text")

    def test_remove_numbers(self):
        text = "This is a text with 123 numbers"
        processed_text = self.text_processor.remove_numbers(text)
        processed_text = self.text_processor.remove_extra_spaces(processed_text)
        self.assertEqual(processed_text, "This is a text with numbers")

    def test_remove_slang_and_shortcuts(self):
        text = "btw, imo, fyi, lol"
        processed_text = self.text_processor.remove_slang_and_shortcuts(text)
        self.assertEqual(processed_text, "by the way, in my opinion, for your information, laugh out loud")

    def test_lemmatize_text(self):
        input_text = "dogs running in the park"
        expected_output = "dog running in the park"
        self.assertEqual(TextProcessor.lemmatize_text(input_text), expected_output)

    def test_process_text(self):
        text = "Check out this website: https://www.example.com and let me know your opinion! lol"
        processed_text = self.text_processor.process_text(text)
        expected_result = "check website let know opinion laugh out loud"
        self.assertEqual(processed_text, expected_result)

if __name__ == '__main__':
    unittest.main()
