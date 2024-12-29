"""
Initialization file for the routes package.
This module organizes and imports all API routes for the ZephyrNet backend.
"""

from fastapi import APIRouter
from .voice import router as voice_router

# Create a main router for the application
api_router = APIRouter()

# Include individual route modules
api_router.include_router(voice_router)

__all__ = ["api_router"]
