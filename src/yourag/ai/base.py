from abc import ABC, abstractmethod

from .openai_llm import get_embedding

class EmbeddingModel(ABC):
    """
    Abstract base class for embedding models.
    """

    def __init__(self):
        pass
    
    @abstractmethod
    def generate_embedding(self, text: str):
        pass
        
class EmbeddingFactory:

    __available_embedding_generators = {
        "openai": "yourag.ai.openai_embedding.OpenAIEmbeddingGenerator",
    }

    def get_embedding_model(self):

        raise NotImplementedError("Subclasses should implement this method.")

    def get_embedding(self, text: str):
        raise NotImplementedError("Subclasses should implement this method.")

    