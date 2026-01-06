"""
Data Models and Schemas
Pydantic models for request/response validation
"""

from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from datetime import datetime
from enum import Enum

# Enums
class DocumentType(str, Enum):
    CONSTITUTION = "constitution"
    STATUTE = "statute"
    CASE_LAW = "case_law"
    HIGH_COURT = "high_court"
    SUPREME_COURT = "supreme_court"

class CitationStatus(str, Enum):
    ACTIVE = "active"
    AMENDED = "amended"
    REPEALED = "repealed"
    UNDER_REVIEW = "under_review"

class ConfidenceLevel(str, Enum):
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

# Request Models
class LegalQueryRequest(BaseModel):
    query: str = Field(..., min_length=3, max_length=1000, description="Legal question or query")
    jurisdiction: Optional[str] = Field(None, description="Jurisdiction filter")
    filters: Optional[Dict[str, Any]] = Field(None, description="Additional filters")

class CitationVerifyRequest(BaseModel):
    citations: List[str] = Field(..., description="List of citations to verify")

class MemorandumRequest(BaseModel):
    issue: str = Field(..., min_length=10, description="Legal issue for memorandum")
    facts: Optional[str] = Field(None, description="Relevant facts")

class DevilsAdvocateRequest(BaseModel):
    answer: str = Field(..., description="Original answer to analyze")
    query: Optional[str] = Field(None, description="Original query")

# Response Models
class Citation(BaseModel):
    id: str
    text: str
    source: str
    section: str
    page: Optional[int] = None
    status: CitationStatus
    effective_date: Optional[str] = None
    amendments: List[str] = []
    confidence: float

class Source(BaseModel):
    document_name: str
    document_type: DocumentType
    section: str
    content: str
    page: Optional[int] = None
    relevance_score: float
    metadata: Dict[str, Any] = {}

class LegalQueryResponse(BaseModel):
    query_id: str
    query: str
    answer: str
    confidence: float
    confidence_level: ConfidenceLevel
    sources: List[Source]
    citations: List[Citation]
    warnings: List[str] = []
    processing_time: float
    timestamp: datetime

class CitationDetail(BaseModel):
    citation_id: str
    full_text: str
    source_document: str
    section: str
    status: CitationStatus
    effective_date: Optional[str]
    amendment_history: List[Dict[str, str]] = []
    related_cases: List[str] = []
    context: Optional[str] = None

class VerificationResult(BaseModel):
    citation: str
    status: CitationStatus
    valid: bool
    confidence: float
    last_updated: str
    amendments: List[str] = []
    warning: Optional[str] = None

class DevilsAdvocateResponse(BaseModel):
    original_answer: str
    counter_arguments: List[str]
    weak_points: List[str]
    contradictory_precedents: List[Source]
    alternative_interpretations: List[str]

class MemorandumResponse(BaseModel):
    memorandum_id: str
    issue: str
    rule: str
    application: str
    conclusion: str
    citations: List[Citation]
    full_text: str
    generated_at: datetime

# Database Models (SQLAlchemy would be used here)
class QueryHistoryDB(BaseModel):
    id: int
    query: str
    answer: str
    confidence: float
    user_id: Optional[int]
    created_at: datetime
    
    class Config:
        from_attributes = True
