"""
Initialization file for the app package.
This module organizes and initializes the backend app.
"""

# Import the FastAPI app instance and related components for use across the app
from .main import app
from .routes import api_router  # Central router that includes all routes
from .services import transcribe_audio, synthesize_speech, translate_text  # Core services

# Expose important components for easy access in other parts of the app
__all__ = ["app", "api_router", "transcribe_audio", "synthesize_speech", "translate_text"]
