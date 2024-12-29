"""
Initialization file for the models package.
This module imports and organizes models for the ZephyrNet backend.
"""

# Import specific models to make them accessible at the package level
from .user import User

# Define the __all__ variable to control what is exported when using `from models import *`
__all__ = ["User"]
