from fastapi import APIRouter, File, UploadFile, HTTPException, Form, Depends
from fastapi.responses import JSONResponse
from typing import Optional
from app.services.speech_to_text import transcribe_audio
from app.services.text_to_audio import synthesize_speech
from googletrans import Translator, LANGUAGES
import uuid
import os

router = APIRouter(
    prefix="/voice",
    tags=["Voice"]
)

# Dependency for Translator
def get_translator():
    return Translator()

# Helper function to validate audio files
def validate_audio_file(file: UploadFile):
    if not file.content_type.startswith("audio/"):
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Please upload an audio file."
        )

# Helper function to validate languages
def validate_languages(source_language: str, target_language: str):
    if source_language not in LANGUAGES or target_language not in LANGUAGES:
        raise HTTPException(
            status_code=400,
            detail="Invalid source or target language. Please use valid language codes."
        )

# Helper function to save uploaded files
async def save_uploaded_file(file: UploadFile, directory: str = "uploads"):
    file_id = str(uuid.uuid4())
    file_path = f"{directory}/{file_id}_{file.filename}"
    os.makedirs(directory, exist_ok=True)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())
    return file_path

@router.post("/transcribe")
async def transcribe_audio_endpoint(audio_file: UploadFile = File(...)):
    """
    Endpoint to transcribe audio to text.
    
    Args:
        audio_file (UploadFile): Audio file uploaded by the user.
    
    Returns:
        JSONResponse: Transcribed text.
    """
    validate_audio_file(audio_file)
    try:
        text = await transcribe_audio(audio_file)
        return JSONResponse(content={"text": text})
    except FileNotFoundError:
        raise HTTPException(status_code=400, detail="Audio file not found or inaccessible.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Transcription failed: {str(e)}")

@router.post("/synthesize")
async def synthesize_speech_endpoint(
    text: str = Form(..., description="Text to convert into speech"),
    language: str = Form("en-US", description="Language code for speech synthesis"),
    voice: Optional[str] = Form(None, description="Voice ID for speech synthesis (optional)")
):
    """
    Endpoint to synthesize text into speech.
    
    Args:
        text (str): The text to be converted into speech.
        language (str): The language code for the speech synthesis (default: "en-US").
        voice (Optional[str]): The specific voice ID to use (if available).
    
    Returns:
        JSONResponse: URL of the generated audio file.
    """
    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text input cannot be empty."
        )
    try:
        audio_url = await synthesize_speech(text, language, voice)
        return JSONResponse(content={"audio_url": audio_url})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Synthesis failed: {str(e)}")

@router.post("/translate")
async def translate_text_endpoint(
    text: str = Form(..., description="Text to translate"),
    source_language: str = Form(..., description="Source language code"),
    target_language: str = Form(..., description="Target language code"),
    translator: Translator = Depends(get_translator)
):
    """
    Endpoint to translate text between languages.
    
    Args:
        text (str): The text to be translated.
        source_language (str): The language code of the source text.
        target_language (str): The language code for the translated text.
    
    Returns:
        JSONResponse: Translated text.
    """
    validate_languages(source_language, target_language)
    if not text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text input cannot be empty."
        )
    try:
        translated_text = translator.translate(text, src=source_language, dest=target_language).text
        return JSONResponse(content={"translated_text": translated_text})
    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Translation error: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")

@router.post("/save_audio")
async def save_audio_endpoint(audio_file: UploadFile = File(...)):
    """
    Endpoint to save an uploaded audio file to the server.
    
    Args:
        audio_file (UploadFile): Audio file uploaded by the user.
    
    Returns:
        JSONResponse: File path where the audio is saved.
    """
    validate_audio_file(audio_file)
    try:
        file_path = await save_uploaded_file(audio_file)
        return JSONResponse(content={"file_path": file_path})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save audio file: {str(e)}")

@router.get("/languages")
async def get_supported_languages():
    """
    Endpoint to retrieve a list of supported languages for translation.
    
    Returns:
        JSONResponse: List of supported languages.
    """
    try:
        return JSONResponse(content={"languages": LANGUAGES})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to retrieve languages: {str(e)}")
