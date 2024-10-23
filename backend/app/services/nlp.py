import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    """
    Preprocesses text for NLP tasks by converting it to lowercase,
    removing punctuation and stop words, and applying lemmatization.

    Args:
        text: The text to preprocess.

    Returns:
        The preprocessed text.
    """
    text = text.lower()
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)


def extract_keywords(text):
    """
    Extracts keywords from a text using a simple bag-of-words approach.

    Args:
        text: The text to extract keywords from.

    Returns:
        A list of keywords.
    """
    text = preprocess_text(text)
    tokens = word_tokenize(text)
    keywords = set(tokens)  # Remove duplicate words
    return list(keywords)


def generate_response(text):
    """
    Generates a response to a given text using a simple rule-based approach.

    Args:
        text: The input text.

    Returns:
        A response text.
    """
    # Example rule-based response generation
    if "weather" in text:
        return "The weather is beautiful today!"
    elif "restaurant" in text:
        return "I know a great Italian restaurant nearby!"
    else:
        return "I understand your request. Can you please rephrase it?"


# You can add more complex NLP techniques like:
# - Named entity recognition
# - Sentiment analysis
# - Intent classification
# - Dialogue management
