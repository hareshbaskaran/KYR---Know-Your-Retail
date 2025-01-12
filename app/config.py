from pydantic_settings import BaseSettings
from enums import LLMProvider

class Settings(BaseSettings):
    app_name: str = "KYR - ChatBot"
    llm_provider: LLMProvider = LLMProvider.GEMINI
    llm_model: str = LLMProvider.GOOGLE_FLAN
    api_key: str
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"

# Instantiate the settings class to access the settings in your application
settings = Settings()
