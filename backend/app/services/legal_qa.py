"""
Legal QA Service
Orchestrates the entire legal question-answering pipeline
"""

from typing import Dict, List, Optional
import uuid
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class LegalQAService:
    """
    Orchestrates the entire legal question-answering pipeline
    """
    
    def __init__(self):
        # Lazy initialization to avoid circular imports
        self.retriever = None
        self.generator = None
        self.verification_service = None
    
    def _ensure_initialized(self):
        """Lazy initialization of components"""
        if self.retriever is None:
            from app.rag.retriever import LegalRetriever
            from app.rag.generator import GroundedGenerator
            from app.services.verification_service import VerificationService
            
            self.retriever = LegalRetriever()
            self.generator = GroundedGenerator()
            self.verification_service = VerificationService()
    
    async def process_query(
        self,
        query: str,
        jurisdiction: str = "all",
        code_type: str = "all",
        year_range: str = "all"
    ) -> Dict:
        """
        Main pipeline: Retrieve → Generate → Verify
        
        Args:
            query: Legal question
            jurisdiction: Jurisdiction filter
            code_type: Legal code filter (constitution, IPC, etc.)
            year_range: Year range filter
        
        Returns:
            Complete query result with answer, sources, and citations
        """
        
        self._ensure_initialized()
        query_id = str(uuid.uuid4())
        
        try:
            # Step 1: Retrieve relevant sources
            filters = {
                'jurisdiction': jurisdiction if jurisdiction != 'all' else None,
                'code_type': code_type if code_type != 'all' else None,
                'year_range': year_range if year_range != 'all' else None
            }
            
            sources = await self.retriever.retrieve(query, filters=filters)
            
            # Step 2: Generate grounded answer
            generation_result = await self.generator.generate(query, sources)
            
            # Step 3: Verify citations
            citations = generation_result['citations']
            verified_citations = await self.verification_service.verify_citations(citations)
            
            return {
                'id': query_id,
                'query': query,
                'answer': generation_result['answer'],
                'sources': sources,
                'citations': verified_citations,
                'confidence': generation_result['confidence'],
                'timestamp': datetime.utcnow().isoformat()
            }
        
        except Exception as e:
            logger.error(f"Query processing failed: {e}", exc_info=True)
            raise
    
    async def generate_devils_advocate(
        self,
        original_answer: str,
        sources: List[Dict]
    ) -> Dict:
        """
        Generate opposing arguments (Devil's Advocate mode)
        
        Args:
            original_answer: The main answer
            sources: Retrieved sources
        
        Returns:
            Opposing arguments and counter-points
        """
        
        self._ensure_initialized()
        
        opposing_prompt = f"""Given this legal answer:
{original_answer}

Generate 3 opposing legal arguments that could be made based on alternative interpretations
of the same law. Show:
1. Counter-argument with legal basis
2. Weakest point in the original argument
3. What the opposing counsel would argue

Be rigorous and grounded in actual legal concepts."""
        
        try:
            # Mock devil's advocate response (replace with actual LLM call)
            return {
                "opposing_arguments": [
                    "Counter-argument 1: Alternative interpretation of the provision...",
                    "Counter-argument 2: Precedent showing different application...",
                    "Counter-argument 3: Exception clause that weakens main argument..."
                ],
                "weak_points": [
                    "The argument relies heavily on a 2015 judgment that was partially overruled in 2023",
                    "Does not address the exception provided in sub-section (2)"
                ],
                "opposing_authority": "counter-precedent",
                "confidence_in_opposition": 0.75
            }
        
        except Exception as e:
            logger.error(f"Devil's advocate generation failed: {e}")
            return {"error": str(e)}
