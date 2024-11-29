import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def preprocess_text(text):
    text = text.lower()
    text = ''.join(c for c in text if c.isalnum() or c.isspace())
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(tokens)

def extract_keywords(text):
    text = preprocess_text(text)
    tokens = word_tokenize(text)
    return list(set(tokens))

def generate_response(text):
    if "weather" in text:
        return "The weather is beautiful today!"
    elif "restaurant" in text:
        return "I know a great Italian restaurant nearby!"
    return "I understand your request. Can you please rephrase it?"
