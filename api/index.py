from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
import sys
import os
from pathlib import Path

# Add backend to Python path
backend_path = Path(__file__).parent.parent / "backend"
sys.path.insert(0, str(backend_path))

# Import core modules
from app.core.legal_database import LegalDatabase
from app.core.query_intent_analyzer import QueryIntentAnalyzer
from app.core.legal_answer_generator import LegalAnswerGenerator
from app.models.schemas import QueryRequest, QueryResponse

# Initialize FastAPI app
app = FastAPI(
    title="Constitutional AI API",
    description="Zero-Hallucination Legal Research Assistant",
    version="1.0.0"
)

# CORS Configuration - Allow all origins for Vercel
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
legal_db = LegalDatabase()
intent_analyzer = QueryIntentAnalyzer()
answer_generator = LegalAnswerGenerator()

@app.get("/")
async def root():
    return {"message": "Constitutional AI API", "status": "running"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy", "service": "Constitutional AI"}

@app.post("/api/v1/query/legal")
async def legal_query(request: QueryRequest):
    """Process legal query and return verified answer"""
    try:
        # Analyze intent
        intent_result = intent_analyzer.analyze_intent(request.query)
        
        if not intent_result["safe_to_answer"]:
            return QueryResponse(
                query=request.query,
                answer="This query appears to seek advice for harmful purposes. This system is designed for educational legal research only.",
                sources=[],
                confidence=0.0,
                safety_check_passed=False,
                processing_time_ms=0.0
            )
        
        # Extract topics and retrieve sources
        topics = intent_result.get("topics", [])
        sources = legal_db.retrieve_relevant_sources(topics, request.query)
        
        if not sources:
            return QueryResponse(
                query=request.query,
                answer="I don't have sufficient verified sources to answer this question. Please try rephrasing or asking about Constitution articles, IPC sections, or landmark Supreme Court cases.",
                sources=[],
                confidence=0.0,
                safety_check_passed=True,
                processing_time_ms=0.0
            )
        
        # Generate comprehensive answer
        answer = answer_generator.generate(request.query, sources, intent_result)
        
        return QueryResponse(
            query=request.query,
            answer=answer["answer"],
            sources=answer["sources"],
            confidence=answer["confidence"],
            safety_check_passed=True,
            processing_time_ms=answer.get("processing_time_ms", 0.0)
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@app.get("/api/v1/query/suggestions")
async def get_suggestions():
    """Get sample query suggestions"""
    return {
        "suggestions": [
            "What does Article 19 guarantee?",
            "What is the punishment for murder under IPC?",
            "What does Article 21 protect?",
            "Explain Section 302 IPC",
            "What did Supreme Court decide in Bachan Singh case?"
        ]
    }

# Wrap FastAPI app for Vercel serverless
handler = Mangum(app, lifespan="off")
