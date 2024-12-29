import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Download necessary NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text: str) -> str:
    """
    Preprocess the input text by:
    - Converting to lowercase
    - Removing non-alphanumeric characters except spaces
    - Tokenizing the text
    - Removing stopwords
    - Lemmatizing each token
    Args:
        text (str): The input text to preprocess.
    Returns:
        str: The preprocessed text.
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove non-alphanumeric characters except spaces
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize tokens
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Return the processed text
    return ' '.join(tokens)

def extract_keywords(text: str) -> list:
    """
    Extract keywords from the text by preprocessing and returning unique tokens.
    Args:
        text (str): The input text to extract keywords from.
    Returns:
        list: List of unique keywords.
    """
    text = preprocess_text(text)
    tokens = word_tokenize(text)
    return list(set(tokens))

def generate_response(text: str) -> str:
    """
    Generate a response based on the input text.
    Args:
        text (str): The user input text.
    Returns:
        str: The response based on keywords in the text.
    """
    # Basic keyword-based response generation
    if "weather" in text:
        return "The weather is beautiful today!"
    elif "restaurant" in text:
        return "I know a great Italian restaurant nearby!"
    return "I understand your request. Can you please rephrase it?"
