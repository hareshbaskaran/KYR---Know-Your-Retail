from enum import Enum

class LLMProvider(str, Enum):
    GOOGLE_FLAN = "google-flan-1.5"
    GEMINI = "gemini"
