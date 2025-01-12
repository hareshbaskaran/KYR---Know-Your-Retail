from pydantic import BaseSettings
from enums import LLMProvider
class Settings(BaseSettings):
    app_name: str = "KYR - ChatBot"
    llm_provider: str = LLMProvider.GEMINI
    llm_model: str = LLMProvider.GOOGLE_FLAN
    api_key: str
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"


# settings = Settings()