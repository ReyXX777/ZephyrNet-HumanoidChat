from fastapi import FastAPI
from app.routes import api_router  # Import the central API router

app = FastAPI()

# Include the central API router, which includes all route modules (voice, etc.)
app.include_router(api_router)

@app.get("/")
def read_root():
    """
    Root endpoint that returns a basic message about the AI Communication Tool Backend.
    Returns:
        dict: A simple message indicating the backend is running.
    """
    return {"message": "AI Communication Tool Backend is running"}
