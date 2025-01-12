from langchain_google_genai import ChatGoogleGenerativeAI
from utils.variables import GOOGLE_API_KEY  # Assuming you have this in your utils
from base_llm import BaseLLMProvider

class GeminiLLMProvider(BaseLLMProvider):
    provider_name = "Gemini"
    model_name = "gemini-1.5-pro"

    def get_llm(self) -> ChatGoogleGenerativeAI:
        """
        This method returns an instance of the ChatGoogleGenerativeAI model.
        """
        return ChatGoogleGenerativeAI(
            model=self.model_name,
            temperature=0.7,
            top_p=0.85,
            google_api_key=GOOGLE_API_KEY
        )
