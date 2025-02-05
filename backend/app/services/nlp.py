import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import string

# Download necessary NLTK resources
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

# Initialize NLTK components
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text: str) -> str:
    """
    Preprocess the input text by:
    - Converting to lowercase
    - Removing punctuation and non-alphanumeric characters except spaces
    - Tokenizing the text
    - Removing stopwords
    - Lemmatizing each token
    Args:
        text (str): The input text to preprocess.
    Returns:
        str: The preprocessed text.
    """
    if not text.strip():
        raise ValueError("Input text cannot be empty or just whitespace.")
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize the text
    tokens = word_tokenize(text)
    
    # Remove stopwords
    tokens = [token for token in tokens if token not in stop_words]
    
    # Lemmatize tokens
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
    if not text.strip():
        raise ValueError("Input text cannot be empty or just whitespace.")
    
    # Preprocess text
    preprocessed_text = preprocess_text(text)
    
    # Tokenize the preprocessed text
    tokens = word_tokenize(preprocessed_text)
    
    # Return unique keywords
    return sorted(set(tokens))  # Sorted for consistency

def generate_response(text: str) -> str:
    """
    Generate a response based on the input text.
    Args:
        text (str): The user input text.
    Returns:
        str: The response based on keywords in the text.
    """
    if not text.strip():
        raise ValueError("Input text cannot be empty or just whitespace.")
    
    # Preprocess text and extract keywords
    keywords = extract_keywords(text)
    
    # Basic keyword-based response generation
    if "weather" in keywords:
        return "The weather is beautiful today! How can I assist you further?"
    elif "restaurant" in keywords:
        return "I know a great Italian restaurant nearby! Would you like directions?"
    elif "help" in keywords:
        return "Sure, I'm here to help! What do you need assistance with?"
    elif "thank" in keywords:
        return "You're welcome! Let me know if you need anything else."
    else:
        return "I understand your request. Can you please provide more details or rephrase?"

def calculate_sentiment_score(text: str) -> int:
    """
    Calculate a simple sentiment score based on the presence of positive or negative words.
    Args:
        text (str): The input text to analyze.
    Returns:
        int: Sentiment score (1 for positive, -1 for negative, 0 for neutral).
    """
    positive_words = {"happy", "good", "great", "awesome", "love"}
    negative_words = {"sad", "bad", "terrible", "hate", "awful"}
    
    # Preprocess text and extract keywords
    keywords = extract_keywords(text)
    
    # Calculate sentiment score
    positive_count = sum(1 for word in keywords if word in positive_words)
    negative_count = sum(1 for word in keywords if word in negative_words)
    
    if positive_count > negative_count:
        return 1
    elif negative_count > positive_count:
        return -1
    else:
        return 0

# Example Usage
if __name__ == "__main__":
    user_input = "Can you recommend a good restaurant nearby?"
    print("User Input:", user_input)
    response = generate_response(user_input)
    print("Response:", response)
    
    sentiment_input = "I feel happy and excited today!"
    sentiment_score = calculate_sentiment_score(sentiment_input)
    print("Sentiment Score:", sentiment_score)
