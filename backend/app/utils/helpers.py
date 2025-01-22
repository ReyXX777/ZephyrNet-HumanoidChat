# ZephyrNet-HumanoidChat/backend/app/utils/helpers.py

from typing import List, Dict, Optional
import hashlib
import uuid
from datetime import datetime
import re

def generate_unique_id() -> str:
    """
    Generate a unique identifier using UUID.
    
    Returns:
        str: A unique identifier.
    """
    return str(uuid.uuid4())

def hash_string(input_string: str) -> str:
    """
    Hash a string using SHA-256 for secure storage or comparison.
    
    Args:
        input_string (str): The string to hash.
    
    Returns:
        str: The hashed string.
    """
    return hashlib.sha256(input_string.encode()).hexdigest()

def validate_email(email: str) -> bool:
    """
    Validate an email address using regex.
    
    Args:
        email (str): The email address to validate.
    
    Returns:
        bool: True if the email is valid, False otherwise.
    """
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(regex, email) is not None

def format_timestamp(timestamp: datetime) -> str:
    """
    Format a datetime object into a human-readable string.
    
    Args:
        timestamp (datetime): The timestamp to format.
    
    Returns:
        str: Formatted timestamp string.
    """
    return timestamp.strftime("%Y-%m-%d %H:%M:%S")

def truncate_text(text: str, max_length: int = 100) -> str:
    """
    Truncate text to a specified maximum length.
    
    Args:
        text (str): The text to truncate.
        max_length (int): The maximum allowed length.
    
    Returns:
        str: Truncated text.
    """
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

def extract_hashtags(text: str) -> List[str]:
    """
    Extract hashtags from a given text.
    
    Args:
        text (str): The text to extract hashtags from.
    
    Returns:
        List[str]: List of extracted hashtags.
    """
    return re.findall(r"#\w+", text)

def calculate_reading_time(text: str, words_per_minute: int = 200) -> int:
    """
    Calculate the estimated reading time for a given text.
    
    Args:
        text (str): The text to calculate reading time for.
        words_per_minute (int): Average words read per minute.
    
    Returns:
        int: Estimated reading time in minutes.
    """
    word_count = len(text.split())
    return max(1, word_count // words_per_minute)

# Example Usage
if __name__ == "__main__":
    # Test unique ID generation
    unique_id = generate_unique_id()
    print("Unique ID:", unique_id)
    
    # Test string hashing
    hashed_string = hash_string("password123")
    print("Hashed String:", hashed_string)
    
    # Test email validation
    email = "test@example.com"
    is_valid = validate_email(email)
    print(f"Is '{email}' valid? {is_valid}")
    
    # Test timestamp formatting
    timestamp = datetime.now()
    formatted_timestamp = format_timestamp(timestamp)
    print("Formatted Timestamp:", formatted_timestamp)
    
    # Test text truncation
    long_text = "This is a very long text that needs to be truncated."
    truncated_text = truncate_text(long_text, 20)
    print("Truncated Text:", truncated_text)
    
    # Test hashtag extraction
    text_with_hashtags = "This is a #test with #hashtags."
    hashtags = extract_hashtags(text_with_hashtags)
    print("Extracted Hashtags:", hashtags)
    
    # Test reading time calculation
    reading_time = calculate_reading_time(" ".join(["word"] * 450))
    print("Estimated Reading Time (minutes):", reading_time)
