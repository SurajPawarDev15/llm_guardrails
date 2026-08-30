from google import genai
from google.genai import errors
from config import (
    GEMINI_API_KEY,
    GEMINI_MODEL,
)

# Create Gemini client
client = genai.Client(
    api_key=GEMINI_API_KEY
)


def generate_response(prompt: str) -> str:
    """Generate a response using Gemini."""
    try:
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt,
        )
        return response.text or ""
    except (errors.ServerError, errors.APIError, TimeoutError, OSError) as exc:
        raise RuntimeError(
            "Gemini model is temporarily unavailable. Please try again later."
        ) from exc

### Thank you ###    