from google import genai
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

    response = client.models.generate_content(
        model=GEMINI_MODEL,
        contents=prompt,
    )
    return response.text or ""