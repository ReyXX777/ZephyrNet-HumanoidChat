# ZephyrNet-HumanoidChat/backend/app/utils/__init__.py

from typing import List, Dict, Optional
import logging
import json
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_interaction(user_id: str, message: str, response: str) -> None:
    """
    Log user interactions for analytics and debugging purposes.
    
    Args:
        user_id (str): Unique identifier for the user.
        message (str): The message sent by the user.
        response (str): The response generated by the system.
    """
    timestamp = datetime.now().isoformat()
    log_entry = {
        "timestamp": timestamp,
        "user_id": user_id,
        "message": message,
        "response": response
    }
    logger.info(json.dumps(log_entry))

def validate_user_input(input_data: Dict) -> Optional[str]:
    """
    Validate user input to ensure it meets required criteria.
    
    Args:
        input_data (Dict): The input data to validate.
    
    Returns:
        Optional[str]: Error message if validation fails, otherwise None.
    """
    if not input_data.get("user_id"):
        return "User ID is required."
    if not input_data.get("message"):
        return "Message cannot be empty."
    if len(input_data["message"]) > 1000:
        return "Message exceeds the maximum allowed length of 1000 characters."
    return None

def format_response(response_data: Dict) -> Dict:
    """
    Format the response data to ensure consistency.
    
    Args:
        response_data (Dict): The response data to format.
    
    Returns:
        Dict: Formatted response data.
    """
    formatted_response = {
        "status": "success",
        "timestamp": datetime.now().isoformat(),
        "data": response_data
    }
    return formatted_response

def generate_error_response(error_message: str, status_code: int) -> Dict:
    """
    Generate a standardized error response.
    
    Args:
        error_message (str): The error message to include.
        status_code (int): The HTTP status code for the error.
    
    Returns:
        Dict: Standardized error response.
    """
    return {
        "status": "error",
        "timestamp": datetime.now().isoformat(),
        "error": {
            "message": error_message,
            "code": status_code
        }
    }

def sanitize_input(input_text: str) -> str:
    """
    Sanitize user input to prevent injection attacks.
    
    Args:
        input_text (str): The input text to sanitize.
    
    Returns:
        str: Sanitized input text.
    """
    # Remove potentially harmful characters
    sanitized_text = "".join(char for char in input_text if char.isalnum() or char in " .,!?-")
    return sanitized_text.strip()

# Example Usage
if __name__ == "__main__":
    # Test logging
    log_interaction("user123", "Hello!", "Hi there! How can I assist you?")
    
    # Test validation
    input_data = {"user_id": "user123", "message": "Hello!"}
    validation_error = validate_user_input(input_data)
    if validation_error:
        print(validation_error)
    
    # Test response formatting
    response_data = {"message": "Hi there! How can I assist you?"}
    formatted_response = format_response(response_data)
    print(formatted_response)
    
    # Test error response
    error_response = generate_error_response("Invalid input", 400)
    print(error_response)
    
    # Test input sanitization
    sanitized_input = sanitize_input("Hello! <script>alert('XSS')</script>")
    print(sanitized_input)
