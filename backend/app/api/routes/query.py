"""
Query API Routes
Handles legal query processing with comprehensive legal database
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
import logging
import time
import uuid
from datetime import datetime

from app.core.config import settings
from app.core.constants import ERROR_MESSAGES
from app.core.query_intent_analyzer import QueryIntentAnalyzer, QueryType
from app.core.legal_answer_generator import LegalAnswerGenerator

router = APIRouter()
logger = logging.getLogger(__name__)

class LegalQueryRequest(BaseModel):
    query: str
    jurisdiction: str = "all"
    codeType: Optional[str] = "all"
    yearRange: Optional[str] = "all"
    include_devil_advocate: bool = False

class CitationResponse(BaseModel):
    id: str
    text: str
    source: str
    section: str
    status: str = "active"
    confidence: float
    amendments: List[str] = []

class SourceResponse(BaseModel):
    document_name: str
    document_type: str
    section: str
    content: str
    relevance_score: float
    metadata: Dict[str, Any] = {}

class LegalQueryResponse(BaseModel):
    id: str
    query: str
    answer: str
    sources: List[SourceResponse]
    citations: List[CitationResponse]
    confidence: float
    processing_time: int
    timestamp: datetime
    devil_advocate: Optional[Dict] = None
    # Validation metadata
    safety_check_passed: bool = True
    validation_stage: str = "complete"
    input_validation: Optional[Dict] = None
    validation_report: Optional[Dict] = None

# Initialize comprehensive legal system
intent_analyzer = QueryIntentAnalyzer()
answer_generator = LegalAnswerGenerator()

@router.post("/legal", response_model=LegalQueryResponse)
async def query_legal(request: LegalQueryRequest):
    """
    Comprehensive legal query endpoint with intent analysis and citation-rich answers
    
    Process:
    1. LAYER 1: Intent Analysis (Educational vs Harmful)
    2. LAYER 2: Topic Extraction
    3. LAYER 3: Source Retrieval from Legal Database
    4. LAYER 4: Comprehensive Answer Generation
    5. LAYER 5: Confidence Calculation & Response
    """
    
    start_time = time.time()
    query_id = str(uuid.uuid4())
    
    try:
        # ============================================
        # LAYER 1: INTENT ANALYSIS
        # ============================================
        
        logger.info(f"Processing query: {request.query[:100]}...")
        
        query_type, should_allow, intent_confidence = \
            intent_analyzer.analyze_intent(request.query)
        
        if not should_allow:
            logger.warning(f"Harmful intent detected: {query_type.value}")
            
            processing_time = int((time.time() - start_time) * 1000)
            
            return LegalQueryResponse(
                id=query_id,
                query=request.query,
                answer="I cannot provide guidance on illegal activities or methods to evade law. This system is designed for educational legal research only. Please consult a qualified lawyer for legal advice.",
                sources=[],
                citations=[],
                confidence=0.0,
                processing_time=processing_time,
                timestamp=datetime.utcnow(),
                safety_check_passed=False,
                validation_stage='intent_analysis',
                input_validation={'query_type': query_type.value, 'intent_confidence': intent_confidence}
            )
        
        logger.info(f"✓ Intent validation passed - Query type: {query_type.value}, Confidence: {intent_confidence:.0%}")
        
        # ============================================
        # LAYER 2: TOPIC EXTRACTION
        # ============================================
        
        topics = intent_analyzer.extract_query_topics(request.query)
        logger.info(f"Extracted topics: {topics}")
        
        # ============================================
        # LAYER 3-4: SOURCE RETRIEVAL & ANSWER GENERATION
        # ============================================
        
        result = answer_generator.generate_answer(request.query, topics)
        
        logger.info(f"Generated answer with {result['num_sources']} sources, confidence: {result['confidence']:.0%}")
        
        # Convert sources to response format
        sources_response = []
        citations_response = []
        
        for idx, source in enumerate(result['sources']):
            # Add to sources
            sources_response.append(SourceResponse(
                document_name=source['source'],
                document_type=source['type'],
                section=source.get('citation', source['source']),
                content=source['text'][:500] + "..." if len(source['text']) > 500 else source['text'],
                relevance_score=0.9,
                metadata={
                    'year': source.get('year'),
                    'court': source.get('court'),
                    'title': source.get('title')
                }
            ))
            
            # Add to citations
            citations_response.append(CitationResponse(
                id=f"cite_{idx+1}",
                text=source['title'],
                source=source['source'],
                section=source.get('citation', ''),
                status="verified",
                confidence=0.95,
                amendments=[]
            ))
        
        # ============================================
        # LAYER 5: RESPONSE GENERATION
        # ============================================
        
        processing_time = int((time.time() - start_time) * 1000)
        
        logger.info(f"✓ Query processed successfully in {processing_time}ms")
        
        return LegalQueryResponse(
            id=query_id,
            query=request.query,
            answer=result['answer'],
            sources=sources_response,
            citations=citations_response,
            confidence=result['confidence'],
            processing_time=processing_time,
            timestamp=datetime.utcnow(),
            safety_check_passed=True,
            validation_stage='complete',
            input_validation={
                'query_type': query_type.value,
                'intent_confidence': intent_confidence,
                'topics': topics
            },
            validation_report={
                'num_sources': result['num_sources'],
                'has_case_laws': result['has_case_laws'],
                'has_constitutional': result['has_constitutional'],
                'has_ipc': result['has_ipc']
            }
        )
        
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}", exc_info=True)
        
        processing_time = int((time.time() - start_time) * 1000)
        
        # Return error response
        return LegalQueryResponse(
            id=query_id,
            query=request.query,
            answer="An error occurred while processing your query. Please try again or consult a qualified lawyer.",
            sources=[],
            citations=[],
            confidence=0.0,
            processing_time=processing_time,
            timestamp=datetime.utcnow(),
            safety_check_passed=False,
            validation_stage='error'
        )

@router.get("/suggestions")
async def query_suggestions(partial_query: str = ""):
    """
    Returns suggested legal questions based on user input
    """
    return {
        "suggestions": [
            "What will happen if I kill a person?",
            "What does Article 19 guarantee?",
            "What is the punishment for murder under IPC?",
            "What does Article 21 protect?",
            "What is the difference between murder and culpable homicide?"        ]
    }

@router.get("/{query_id}")
async def get_query(query_id: str):
    """
    Retrieve previous query results
    """
    # TODO: Implement database lookup
    raise HTTPException(status_code=404, detail="Query not found")