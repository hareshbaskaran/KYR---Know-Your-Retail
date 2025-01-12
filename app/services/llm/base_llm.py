from abc import ABC, abstractmethod
from langchain_core.language_models import BaseChatModel

class BaseLLMProvider(ABC):
    provider_name: str
    model_name: str

    @abstractmethod
    def get_llm(self) -> BaseChatModel:
        """
        This method should be implemented by concrete LLM providers to return
        an instance of a specific LLM (Language Model) class.
        """
        pass
