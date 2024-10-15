from fastapi import FastAPI
from .routes import voice

app = FastAPI()

app.include_router(voice.router)

@app.get("/")
def read_root():
    return {"message": "AI Communication Tool Backend"}

