"""
Database Models
SQLAlchemy ORM models
"""

from sqlalchemy import Column, Integer, String, Float, DateTime, JSON, Text, Boolean
from sqlalchemy.sql import func
from app.database.session import Base

class QueryHistory(Base):
    """
    Stores query history
    """
    __tablename__ = "query_history"
    
    id = Column(Integer, primary_key=True, index=True)
    query_id = Column(String, unique=True, index=True)
    query = Column(Text, nullable=False)
    answer = Column(Text)
    confidence = Column(Float)
    user_id = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    processing_time = Column(Integer)  # milliseconds
    metadata = Column(JSON)

class CitationStatus(Base):
    """
    Stores citation verification status
    """
    __tablename__ = "citation_status"
    
    id = Column(Integer, primary_key=True, index=True)
    citation_id = Column(String, unique=True, index=True)
    section = Column(String, nullable=False)
    source = Column(String, nullable=False)
    status = Column(String, default="active")  # active, amended, repealed
    last_verified = Column(DateTime(timezone=True), server_default=func.now())
    amendments = Column(JSON, default=[])
    effective_date = Column(String)
    metadata = Column(JSON)

class LegalDocument(Base):
    """
    Stores legal documents metadata
    """
    __tablename__ = "legal_documents"
    
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(String, unique=True, index=True)
    title = Column(String, nullable=False)
    source = Column(String, nullable=False)
    section = Column(String)
    content = Column(Text, nullable=False)
    authority_level = Column(String)  # supreme, high_court, statute
    jurisdiction = Column(String)
    code_type = Column(String)
    effective_date = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    metadata = Column(JSON)

class User(Base):
    """
    User accounts
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    metadata = Column(JSON)
