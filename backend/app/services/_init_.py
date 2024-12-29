"""
Initialization file for the services package.
This module organizes and imports all service functions for the ZephyrNet backend.
"""

# Import specific services to make them accessible at the package level
from .speech_to_text import transcribe_audio
from .text_to_speech import synthesize_speech
from .translation import translate_text

# Define the __all__ variable to control what is exported when using `from services import *`
__all__ = ["transcribe_audio", "synthesize_speech", "translate_text"]
