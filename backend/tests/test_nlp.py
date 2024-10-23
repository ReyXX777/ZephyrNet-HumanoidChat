import unittest

from app.services.nlp import (
    preprocess_text,
    extract_keywords,
    generate_response,
)


class TestNLP(unittest.TestCase):

    def test_preprocess_text(self):
        text = "This is a test sentence. It has some punctuation! And numbers: 123."
        processed_text = preprocess_text(text)
        self.assertEqual(processed_text, "this is a test sentence it has some punctuation and numbers")

    def test_extract_keywords(self):
        text = "I'm looking for a restaurant in New York City that serves Italian food."
        keywords = extract_keywords(text)
        self.assertIn("restaurant", keywords)
        self.assertIn("new york city", keywords)
        self.assertIn("italian food", keywords)

    def test_generate_response(self):
        # You need to mock the chatbot response generation logic here
        # This is just an example
        text = "What's the weather like today?"
        response = generate_response(text)
        self.assertIsNotNone(response)
        self.assertNotEqual(response, "")


if __name__ == '__main__':
    unittest.main()
