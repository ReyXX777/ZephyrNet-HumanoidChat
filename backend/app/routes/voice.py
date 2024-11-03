from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
from typing import List, Optional
from app.services.speech_to_text import transcribe_audio
from app.services.text_to_speech import synthesize_speech
from googletrans import Translator, LANGUAGES

router = APIRouter(prefix="/voice", tags=["Voice"])


@router.post("/transcribe")
async def transcribe_audio_endpoint(audio_file: UploadFile = File(...)):
    """
    Transcribes an audio file to text using a speech-to-text service.

    Args:
        audio_file: The audio file to transcribe.

    Returns:
        A JSON response containing the transcribed text or an error message.
    """
    try:
        text = await transcribe_audio(audio_file)
        return JSONResponse(content={"text": text})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/synthesize")
async def synthesize_speech_endpoint(
    text: str, 
    language: str = "en-US", 
    voice: Optional[str] = None
):
    """
    Synthesizes speech from text using a text-to-speech service.

    Args:
        text: The text to synthesize.
        language: The language of the text.
        voice: The voice to use for synthesis.

    Returns:
        A JSON response containing a download URL for the synthesized speech audio file or an error message.
    """
    try:
        audio_url = await synthesize_speech(text, language, voice)
        return JSONResponse(content={"audio_url": audio_url})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/translate")
async def translate_text_endpoint(
    text: str, 
    source_language: str, 
    target_language: str
):
    """
    Translates text from one language to another.

    Args:
        text: The text to translate.
        source_language: The language of the text to translate.
        target_language: The language to translate to.

    Returns:
        A JSON response containing the translated text or an error message.
    """
    # Validate source and target languages
    if source_language not in LANGUAGES or target_language not in LANGUAGES:
        raise HTTPException(status_code=400, detail="Invalid source or target language.")

    try:
        translator = Translator()
        translated_text = translator.translate(text, src=source_language, dest=target_language).text
        return JSONResponse(content={"translated_text": translated_text})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
