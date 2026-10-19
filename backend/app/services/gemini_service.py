
from google import genai
from google.genai import types

from app.config import GEMINI_API_KEY, MODEL_NAME


def generate_response(
    prompt: str,
    temperature: float = 0.3,
) -> str:
    """
    Generate a response from Gemini for a given prompt.
    """

    if not GEMINI_API_KEY:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. "
            "Configure it in your backend .env file."
        )

    if not 0.0 <= temperature <= 2.0:
        raise ValueError(
            "Temperature must be between 0.0 and 2.0."
        )

    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=temperature,
        ),
    )

    if not response.text:
        raise RuntimeError(
            "Gemini returned no text response."
        )

    return response.text
