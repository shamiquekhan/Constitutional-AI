"""
Configuration Settings
Loads environment variables and provides app configuration
"""

from pydantic_settings import BaseSettings
from typing import List
import os
from functools import lru_cache
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """Application Settings"""
    
    # Application
    APP_NAME: str = "Constitutional AI"
    API_V1_STR: str = "/api/v1"
    VERSION: str = "1.0.0"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # CORS
    ALLOWED_ORIGINS: List[str] = [
        "http://localhost:3000",
        "http://localhost:3001",
    ]
    
    # OpenAI / LLM
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    LLM_MODEL: str = os.getenv("LLM_MODEL", "gpt-4-turbo-preview")
    LLM_TEMPERATURE: float = 0.1  # Low temperature for legal accuracy
    LLM_MAX_TOKENS: int = 2048
    
    # Pinecone Vector DB
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY", "")
    PINECONE_ENVIRONMENT: str = os.getenv("PINECONE_ENVIRONMENT", "prod")
    PINECONE_INDEX_NAME: str = os.getenv("PINECONE_INDEX_NAME", "constitutional-ai")
    PINECONE_METRIC: str = "cosine"
    
    # Database
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL",
        "postgresql://user:password@localhost:5432/constitutional_ai"
    )
    SQLALCHEMY_ECHO: bool = False
    
    # Redis
    REDIS_URL: str = os.getenv("REDIS_URL", "redis://localhost:6379")
    CACHE_TTL: int = 3600  # 1 hour
    
    # Elasticsearch
    ELASTICSEARCH_URL: str = os.getenv("ELASTICSEARCH_URL", "http://localhost:9200")
    
    # RAG Configuration
    CHUNK_SIZE: int = 500
    CHUNK_OVERLAP: int = 100
    RETRIEVAL_K: int = 10  # Number of sources to retrieve
    TOP_K_RESULTS: int = 5
    SIMILARITY_THRESHOLD: float = 0.7
    CONFIDENCE_THRESHOLD: float = 0.6  # Min confidence to generate answer
    
    # Feature Flags
    ENABLE_DEVIL_ADVOCATE: bool = os.getenv("ENABLE_DEVIL_ADVOCATE", "true").lower() == "true"
    ENABLE_MEMORANDUM_GENERATOR: bool = os.getenv("ENABLE_MEMORANDUM_GENERATOR", "true").lower() == "true"
    ENABLE_CITATION_VERIFICATION: bool = os.getenv("ENABLE_CITATION_VERIFICATION", "true").lower() == "true"
    
    # Rate Limiting
    RATE_LIMIT_PER_MINUTE: int = 60
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    class Config:
        case_sensitive = True
        env_file = ".env"

@lru_cache()
def get_settings():
    """Get cached settings instance"""
    return Settings()

# Create settings instance
settings = get_settings()
