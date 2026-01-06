"""
Embedding Service
Generates vector embeddings for text
"""

from typing import List, Union
import logging

logger = logging.getLogger(__name__)

class EmbeddingService:
    """
    Service for generating text embeddings
    """
    
    def __init__(self, model_name: str = "text-embedding-ada-002"):
        self.model_name = model_name
        self.initialized = False
        
        try:
            # Initialize OpenAI embeddings
            # from langchain_openai import OpenAIEmbeddings
            # self.embeddings = OpenAIEmbeddings(model=model_name)
            
            logger.info(f"EmbeddingService initialized with model: {model_name}")
            self.initialized = True
        except Exception as e:
            logger.error(f"Failed to initialize EmbeddingService: {e}")
    
    def encode(self, text: Union[str, List[str]]) -> Union[List[float], List[List[float]]]:
        """
        Generate embeddings for text
        
        Args:
            text: Single text string or list of texts
        
        Returns:
            Embedding vector(s)
        """
        
        try:
            # if isinstance(text, str):
            #     return self.embeddings.embed_query(text)
            # else:
            #     return self.embeddings.embed_documents(text)
            
            # Mock embedding (replace with actual embedding generation)
            if isinstance(text, str):
                return [0.1] * 1536  # OpenAI embedding dimension
            else:
                return [[0.1] * 1536 for _ in text]
        
        except Exception as e:
            logger.error(f"Embedding generation error: {e}")
            return [] if isinstance(text, list) else [0.0] * 1536
