from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import api_router  # Import the central API router

# Initialize FastAPI app
app = FastAPI(
    title="AI Communication Tool",
    description="Backend API for the AI Communication Tool, providing voice, text, and translation functionalities.",
    version="1.0.0",
    docs_url="/docs",  # Customize the URL for Swagger documentation
    redoc_url="/redoc"  # Customize the URL for ReDoc documentation
)

# Add CORS middleware for cross-origin requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update to specific origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the central API router, which includes all route modules (voice, etc.)
app.include_router(api_router)

@app.get("/", tags=["Root"])
def read_root():
    """
    Root endpoint that returns a basic message about the AI Communication Tool Backend.
    Returns:
        dict: A simple message indicating the backend is running.
    """
    return {"message": "AI Communication Tool Backend is running successfully!"}

@app.get("/health", tags=["Health Check"])
def health_check():
    """
    Health check endpoint to verify the application's status.
    Returns:
        dict: A message indicating the application is healthy.
    """
    return {"status": "healthy", "version": "1.0.0", "uptime": "Service is operational."}

@app.get("/info", tags=["System Info"])
def system_info():
    """
    System information endpoint to provide details about the application and environment.
    Returns:
        dict: A dictionary containing system information.
    """
    import platform
    import os
    return {
        "system": platform.system(),
        "node": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "python_version": platform.python_version(),
        "environment": os.getenv("ENVIRONMENT", "development")
    }

@app.post("/feedback", tags=["Feedback"])
def submit_feedback(feedback: str):
    """
    Endpoint to submit user feedback.
    Args:
        feedback (str): The feedback provided by the user.
    Returns:
        dict: A confirmation message.
    """
    # Log feedback (in a real application, this would be saved to a database)
    print(f"Feedback received: {feedback}")
    return {"message": "Thank you for your feedback!"}
