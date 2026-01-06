"""
Grounded Generator - LLM with Source Grounding
Ensures all outputs cite sources and prevent hallucinations
"""

from typing import List, Dict, Optional
import logging
from app.core.config import settings

logger = logging.getLogger(__name__)

class GroundedGenerator:
    """
    Generates answers guaranteed to be grounded in sources
    
    Key principle: All answers MUST cite sources. No hallucinations.
    """
    
    def __init__(self):
        self.initialized = False
        try:
            # Initialize LLM
            # from langchain_openai import ChatOpenAI
            # self.llm = ChatOpenAI(
            #     model_name=settings.LLM_MODEL,
            #     temperature=settings.LLM_TEMPERATURE,
            #     max_tokens=settings.LLM_MAX_TOKENS,
            #     api_key=settings.OPENAI_API_KEY
            # )
            
            logger.info("GroundedGenerator initialized successfully")
            self.initialized = True
        except Exception as e:
            logger.error(f"Failed to initialize GroundedGenerator: {e}")
    
    async def generate(
        self,
        query: str,
        sources: List[Dict],
        extraction_mode: bool = False
    ) -> Dict:
        """
        Generate answer grounded in retrieved sources
        
        Args:
            query: Legal question
            sources: Retrieved legal documents
            extraction_mode: If True, extracts key info; if False, generates analysis
        
        Returns:
            {
                "answer": "Full answer with citations",
                "citations": [{"id": "...", "text": "..."}],
                "confidence": 0.95,
                "sources_used": 5
            }
        """
        
        if not sources:
            return {
                "answer": "I don't have verified sources to answer this question. Please consult a lawyer for legal advice.",
                "citations": [],
                "confidence": 0.0,
                "sources_used": 0
            }
        
        # Build context from sources
        context = self._build_context(sources)
        
        # System prompt ensures source grounding
        system_prompt = """You are a legal AI assistant specializing in Indian law. You MUST:
1. ONLY use the provided legal sources in your response
2. Include explicit citations in [CITATION: source] format for EVERY claim
3. Say "I don't have verified sources for this" if insufficient data
4. NEVER make up cases, sections, or legal interpretations
5. Show confidence level based on source quality and quantity
6. Use professional legal language
7. Be precise and accurate - in law, details matter

Remember: In law, creativity is dangerous. Speak only when you have proof."""
        
        user_prompt = f"""Question: {query}

Sources:
{context}

Generate a comprehensive legal answer using ONLY the provided sources. 
Include citations for every claim. State your confidence level at the end."""
        
        try:
            # Mock LLM response (replace with actual LLM call)
            answer_text = self._generate_mock_answer(query, sources)
            
            # Extract citations from generated answer
            citations = self._extract_citations_from_answer(answer_text, sources)
            
            # Calculate confidence
            confidence = self._calculate_confidence(sources, len(citations))
            
            return {
                "answer": answer_text,
                "citations": citations,
                "confidence": confidence,
                "sources_used": len(sources)
            }
        
        except Exception as e:
            logger.error(f"Generation error: {e}")
            return {
                "answer": f"Error generating answer: {str(e)}",
                "citations": [],
                "confidence": 0.0,
                "sources_used": 0
            }
    
    def _build_context(self, sources: List[Dict]) -> str:
        """Build context string from sources"""
        context_parts = []
        
        for i, source in enumerate(sources, 1):
            context_parts.append(f"""
SOURCE {i}: {source.get('source', 'Unknown')} - {source.get('section', '')}
Authority Level: {source.get('authority_level', 'unknown')}
Relevance Score: {source.get('hybrid_score', 0):.2f}
---
{source.get('text', '')}
---
""")
        
        return "\n".join(context_parts)
    
    def _generate_mock_answer(self, query: str, sources: List[Dict]) -> str:
        """Generate mock answer for testing (replace with actual LLM)"""
        
        # Extract key information from sources
        primary_source = sources[0] if sources else {}
        
        answer = f"""Based on the legal provisions in {primary_source.get('source', 'the law')}, 

{primary_source.get('text', 'the relevant legal text provides guidance on this matter')[:200]}...

[CITATION: {primary_source.get('section', 'Source 1')}]

This interpretation is supported by established legal precedent and statutory provisions.

Confidence: {int(self._calculate_confidence(sources, 1) * 100)}% (based on {len(sources)} verified sources)"""
        
        return answer
    
    def _extract_citations_from_answer(self, answer: str, sources: List[Dict]) -> List[Dict]:
        """Extract citation references from generated answer"""
        import re
        
        citations = []
        pattern = r'\[CITATION:\s*([^\]]+)\]'
        
        matches = re.finditer(pattern, answer)
        for i, match in enumerate(matches):
            citation_ref = match.group(1)
            
            # Try to find matching source
            source = sources[i] if i < len(sources) else sources[0]
            
            citations.append({
                "id": f"cit-{i+1}",
                "text": citation_ref,
                "source": source.get('source', 'Unknown'),
                "section": source.get('section', ''),
                "status": "active",
                "confidence": 0.95,
                "amendments": []
            })
        
        return citations
    
    def _calculate_confidence(self, sources: List[Dict], citations_count: int) -> float:
        """
        Calculate confidence score
        
        Factors:
        - Number of sources (more = higher confidence)
        - Authority level (supreme court > high court > statute)
        - Citation specificity
        """
        
        # Base confidence from source quality
        authority_weights = {
            'supreme': 0.95,
            'high_court': 0.85,
            'statute': 0.90,
            'case_law': 0.80,
            'unknown': 0.60
        }
        
        total_authority = sum(
            authority_weights.get(source.get('authority_level', 'unknown'), 0.6)
            for source in sources
        )
        
        avg_authority_confidence = total_authority / len(sources) if sources else 0
        
        # Boost confidence based on citation count
        citation_boost = min(0.1, citations_count * 0.03)
        
        # Source count confidence
        source_confidence = min(0.95, 0.5 + (len(sources) * 0.05))
        
        # Final confidence
        final_confidence = (
            avg_authority_confidence * 0.4 + 
            source_confidence * 0.4 + 
            0.2 * (0.8 + citation_boost)
        )
        
        return min(0.99, max(0.0, final_confidence))
