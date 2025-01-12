from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "KYR - ChatBot"
    llm_provider: str = "google-flan-1.5"
    api_key: str
    host: str = "0.0.0.0"
    port: int = 8000

    class Config:
        env_file = ".env"


# settings = Settings()