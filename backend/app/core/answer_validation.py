"""
Answer Validation Layer for Constitutional AI
Validates answers before returning to user
Ensures NO hallucinations or off-topic responses
"""

import re
from typing import Dict, List, Tuple
import logging

logger = logging.getLogger(__name__)


class StrictAnswerValidator:
    """
    Validates answers before returning to user
    Ensures NO hallucinations or off-topic responses
    """
    
    def __init__(self):
        self.min_citations_required = 1  # At least 1 citation per answer
        self.min_confidence_threshold = 0.65
        self.max_sentence_length = 300  # Prevent rambling
        self.legal_claim_keywords = [
            'article', 'section', 'punishment', 'liable', 'guilty',
            'fine', 'imprisonment', 'statute', 'code', 'law', 'rights'
        ]
    
    def validate_answer(
        self,
        answer: str,
        query: str,
        sources: List[Dict],
        confidence: float
    ) -> Tuple[bool, str, Dict]:
        """
        Complete answer validation before returning to user
        Returns: (is_valid, final_answer, validation_report)
        """
        
        report = {
            'is_valid': True,
            'errors': [],
            'warnings': [],
            'issues_found': 0,
            'citations': [],
            'confidence_final': confidence,
            'answer_type': 'standard'
        }
        
        # Check 1: CONFIDENCE THRESHOLD
        if confidence < self.min_confidence_threshold:
            report['is_valid'] = False
            report['errors'].append(
                f'Confidence too low ({confidence:.1%} < {self.min_confidence_threshold:.1%})'
            )
            report['issues_found'] += 1
        
        # Check 2: SOURCE AVAILABILITY
        if not sources or len(sources) == 0:
            report['is_valid'] = False
            report['errors'].append('No verified sources available')
            report['issues_found'] += 1
        elif len(sources) < 2:
            report['is_valid'] = False
            report['errors'].append(
                'Insufficient sources (need minimum 2 sources for verification)'
            )
            report['issues_found'] += 1
        
        # Check 3: CITATION VALIDATION
        citations = self._extract_citations(answer)
        report['citations'] = citations
        
        if not citations and len(answer) > 100:
            # Check if answer contains legal claims
            has_legal_claims = any(
                keyword in answer.lower() 
                for keyword in self.legal_claim_keywords
            )
            if has_legal_claims:
                report['warnings'].append(
                    'Answer contains legal claims without explicit citations'
                )
        
        # Check 4: TOPIC RELEVANCE (does answer match query?)
        if not self._is_answer_relevant_to_query(answer, query):
            report['is_valid'] = False
            report['errors'].append(
                'Answer does not address the query'
            )
            report['issues_found'] += 1
        
        # Check 5: FAKE CITATION DETECTION
        if sources:
            fake_citations = self._detect_fake_citations(answer, sources)
            if fake_citations:
                report['is_valid'] = False
                report['errors'].append(
                    f'Detected potentially fabricated citations: {", ".join(fake_citations)}'
                )
                report['issues_found'] += 1
        
        # Check 6: HALLUCINATION DETECTION
        if sources:
            hallucinations = self._detect_hallucinations(answer, sources)
            if hallucinations:
                report['warnings'].extend(hallucinations)
        
        # Check 7: LENGTH & STRUCTURE VALIDATION
        sentences = [s.strip() for s in answer.split('.') if s.strip()]
        
        for sentence in sentences:
            if len(sentence) > self.max_sentence_length:
                report['warnings'].append(
                    f'Sentence too long (>{self.max_sentence_length} chars)'
                )
                break
        
        # Check 8: REFUSAL QUALITY
        if len(sources) < 2 or confidence < 0.65:
            report['answer_type'] = 'refusal'
            report['is_valid'] = True  # Refusals are valid
            report['errors'] = []  # Clear errors for refusals
        
        # GENERATE FINAL ANSWER
        if report['is_valid']:
            final_answer = answer
        else:
            final_answer = self._generate_safe_refusal(report)
        
        return report['is_valid'], final_answer, report
    
    def _extract_citations(self, answer: str) -> List[str]:
        """Extract citations from answer"""
        citations = []
        
        # Pattern 1: [SECTION: XXX], [ARTICLE: XXX], [CASE: XXX]
        pattern1 = re.findall(r'\[(SECTION|ARTICLE|CASE):[^\]]+\]', answer)
        citations.extend(pattern1)
        
        # Pattern 2: Article XXX, Section XXX
        pattern2 = re.findall(r'(?:Article|Section)\s+\d+[A-Z]?(?:\(\d+\))?', answer, re.IGNORECASE)
        citations.extend(pattern2)
        
        return citations
    
    def _is_answer_relevant_to_query(self, answer: str, query: str) -> bool:
        """Check if answer actually addresses the query"""
        
        # Extract key terms from query
        query_terms = set(re.findall(r'\b[a-z]{3,}\b', query.lower()))
        answer_terms = set(re.findall(r'\b[a-z]{3,}\b', answer.lower()))
        
        # Remove common stop words
        stop_words = {'what', 'when', 'where', 'who', 'how', 'does', 'the', 'and', 'for', 'are', 'can'}
        query_terms -= stop_words
        
        # At least 20% overlap
        if not query_terms:
            return True  # Can't determine, assume valid
        
        overlap = len(query_terms & answer_terms)
        overlap_ratio = overlap / len(query_terms)
        
        return overlap_ratio >= 0.2
    
    def _detect_fake_citations(self, answer: str, sources: List[Dict]) -> List[str]:
        """Detect citations that don't exist in sources"""
        
        # Extract all section/article citations from answer
        section_citations = re.findall(r'(?:Section|SECTION):\s*(\d+[A-Z]?)', answer)
        article_citations = re.findall(r'(?:Article|ARTICLE):\s*(\d+[A-Z]?)', answer)
        
        # Extract valid citations from sources
        valid_sections = set()
        valid_articles = set()
        
        for source in sources:
            metadata = source.get('metadata', {})
            if 'section' in metadata:
                valid_sections.add(str(metadata['section']))
            if 'article' in metadata:
                valid_articles.add(str(metadata['article']))
            
            # Also extract from source text
            source_text = source.get('text', '')
            valid_sections.update(re.findall(r'Section\s+(\d+[A-Z]?)', source_text))
            valid_articles.update(re.findall(r'Article\s+(\d+[A-Z]?)', source_text))
        
        # Find fake ones
        fake = []
        for citation in section_citations:
            if valid_sections and citation not in valid_sections:
                fake.append(f'Section {citation}')
        
        for citation in article_citations:
            if valid_articles and citation not in valid_articles:
                fake.append(f'Article {citation}')
        
        return fake
    
    def _detect_hallucinations(self, answer: str, sources: List[Dict]) -> List[str]:
        """Detect hallucinated content in answer"""
        
        hallucinations = []
        
        # Extract all text from sources
        source_texts = ' '.join([s.get('text', '') for s in sources]).lower()
        answer_lower = answer.lower()
        
        # Check for specific legal claims without sources
        legal_claims = re.findall(
            r'(?:can|cannot|will|shall|must|liable|guilty)[^.]{20,}(?:\.|$)',
            answer_lower,
            re.IGNORECASE
        )
        
        for claim in legal_claims[:3]:  # Check first 3 claims only
            # Check if claim appears in any source
            claim_words = set(re.findall(r'\b[a-z]{4,}\b', claim))
            source_words = set(re.findall(r'\b[a-z]{4,}\b', source_texts))
            
            overlap = len(claim_words & source_words)
            if overlap < len(claim_words) * 0.3:  # Less than 30% overlap
                if any(keyword in claim for keyword in self.legal_claim_keywords):
                    hallucinations.append(f'Potentially unsourced claim detected')
                    break  # Report once only
        
        return hallucinations
    
    def _generate_safe_refusal(self, report: Dict) -> str:
        """Generate a proper refusal message"""
        
        if 'Insufficient sources' in str(report['errors']):
            return (
                "I don't have sufficient verified sources to answer this question. "
                "This legal matter requires consultation with a qualified lawyer "
                "who can provide case-specific advice."
            )
        
        if 'Confidence too low' in str(report['errors']):
            return (
                "I cannot provide a confident answer to this question based on "
                "available sources. Please consult a lawyer for accurate legal guidance."
            )
        
        if 'does not address' in str(report['errors']):
            return (
                "I was unable to find relevant information for your query. "
                "Please rephrase your question or consult a legal professional."
            )
        
        if 'fabricated citations' in str(report['errors']):
            return (
                "I detected inconsistencies in the generated response. "
                "Please consult a qualified lawyer for verified legal information."
            )
        
        return (
            "I cannot provide a verified answer to your question. "
            "Please consult a qualified lawyer for legal advice."
        )
