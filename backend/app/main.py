"""
FastAPI Application Entry Point
Constitutional AI - Legal Research Assistant
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import logging
import uvicorn

from app.core.config import settings
from app.api.routes import query, citations, verification, memorandum, devils_advocate

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize FastAPI app
app = FastAPI(
    title="Constitutional AI API",
    description="Zero-Hallucination Legal Research Assistant API",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://yourdomain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(query.router, prefix="/api/v1/query", tags=["Query"])
app.include_router(citations.router, prefix="/api/v1/citations", tags=["Citations"])
app.include_router(verification.router, prefix="/api/v1/verification", tags=["Verification"])
app.include_router(memorandum.router, prefix="/api/v1/memorandum", tags=["Memorandum"])
app.include_router(devils_advocate.router, prefix="/api/v1/devils-advocate", tags=["Devil's Advocate"])

# Startup event
@app.on_event("startup")
async def startup_event():
    """Initialize services on startup"""
    logger.info("Starting Constitutional AI API...")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    # Initialize database tables
    # from app.database.session import engine, Base
    # Base.metadata.create_all(bind=engine)

# Health check endpoint
@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "version": "1.0.0",
        "service": "Constitutional AI API",
        "environment": settings.ENVIRONMENT
    }

# Root endpoint
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Constitutional AI - Legal Research Assistant API",
        "version": "1.0.0",
        "docs": "/api/docs",
        "tagline": "In law, creativity is dangerous. Constitutional AI ensures that AI speaks only when it has proof."
    }

# Global error handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Handle all uncaught exceptions"""
    logger.error(f"Unhandled error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "type": str(type(exc).__name__)
        }
    )

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
