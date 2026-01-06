"""
Query Intent Analyzer - Distinguishes Educational Questions from Harmful Intent
"""

import re
from enum import Enum
from typing import Tuple, Dict, List


class QueryType(Enum):
    """Distinguish between questions ABOUT legal consequences vs. SEEKING help to commit crime"""
    
    # VALID EDUCATIONAL QUESTIONS
    LEGAL_CONSEQUENCE_QUESTION = "asking_about_legal_consequences"
    PUNISHMENT_INQUIRY = "asking_about_punishment"
    CASE_LAW_INQUIRY = "asking_about_case_law"
    
    # INVALID - SEEKING HELP WITH CRIME
    HOW_TO_COMMIT = "how_to_commit_crime"
    EVADE_LAW = "seeking_to_evade_law"
    HARMFUL_INTENT = "explicit_harmful_intent"


class QueryIntentAnalyzer:
    """
    Distinguishes between:
    1. Educational/informational legal questions (ALLOW)
    2. Harmful intent / seeking help to commit crime (BLOCK)
    """
    
    def __init__(self):
        # Educational intent patterns (ALLOW)
        self.educational_patterns = [
            r'\b(what|which)\s+(happens?|occurs?|is|are)\s+(?:if|when)',  # "what happens if"
            r'\b(what\s+)?(punishment|consequence|penalty|sentence)',      # "what punishment"
            r'\b(define|explain|tell)\s+(me\s+)?(about)',                  # "explain about"
            r'\b(section|article|case|law|act)',                           # "section 302"
            r'\b(supreme\s+court|high\s+court|case\s+law|precedent)',      # "supreme court case"
            r'\blegal\s+(consequence|implication|ramification)',           # "legal consequences"
            r'\bunder\s+(ipc|crpc|indian\s+law)',                          # "under IPC"
        ]
        
        # Criminal intent patterns (BLOCK)
        self.criminal_intent_patterns = [
            r'\bhow\s+(to|can\s+i)\s+(kill|murder|harm|poison|stab)',      # "how to kill"
            r'\bways?\s+to\s+(kill|harm|poison|murder)',                   # "ways to kill"
            r'\b(help|teach)\s+(me\s+)?(to|how)\s+(kill|harm)',            # "help me kill"
            r'\bi\s+(want|need|plan)\s+to\s+(kill|harm|poison)',           # "I want to kill"
            r'\bcan\s+you\s+(help|teach)\s+(me\s+)?(kill|harm)',           # "can you help me kill"
            r'\bhow\s+(do\s+i|can\s+i)\s+(?:escape|evade|avoid)\s+(?:law|police|arrest)',  # "how do I escape law"
            r'\bwithout\s+(getting\s+)?(caught|arrest)',                   # "without getting caught"
            r'\bget\s+away\s+with\s+(murder|killing|crime)',               # "get away with murder"
        ]
    
    def analyze_intent(self, query: str) -> Tuple[QueryType, bool, float]:
        """
        Returns: (query_type, should_allow, confidence)
        
        True = Answer the question (educational)
        False = Block the question (harmful intent)
        """
        
        query_lower = query.lower()
        
        # ===== CHECK 1: Harmful Intent Patterns =====
        for pattern in self.criminal_intent_patterns:
            if re.search(pattern, query_lower):
                return QueryType.HARMFUL_INTENT, False, 0.95
        
        # ===== CHECK 2: Educational Intent Patterns =====
        educational_matches = 0
        for pattern in self.educational_patterns:
            if re.search(pattern, query_lower):
                educational_matches += 1
        
        if educational_matches >= 2:
            # Strong educational intent
            return QueryType.LEGAL_CONSEQUENCE_QUESTION, True, 0.9
        elif educational_matches >= 1:
            # Likely educational
            return QueryType.LEGAL_CONSEQUENCE_QUESTION, True, 0.7
        
        # ===== CHECK 3: Default to Educational if about legal terms =====
        legal_terms = ['section', 'article', 'punishment', 'case law', 'supreme court', 
                      'ipc', 'crpc', 'constitution', 'judgment', 'precedent']
        if any(term in query_lower for term in legal_terms):
            return QueryType.LEGAL_CONSEQUENCE_QUESTION, True, 0.75
        
        # Cannot determine - default to educational for legal research tool
        return QueryType.LEGAL_CONSEQUENCE_QUESTION, True, 0.5
    
    def extract_query_topics(self, query: str) -> List[str]:
        """Extract legal topics from query for database retrieval"""
        
        topics = []
        query_lower = query.lower()
        
        # Map keywords to legal topics
        keyword_map = {
            'killing': ['murder', 'punishment', 'death', 'life'],
            'kill': ['murder', 'punishment', 'death', 'life'],
            'murder': ['murder', 'punishment', 'death'],
            'death': ['death', 'punishment'],
            'punishment': ['punishment'],
            'prison': ['imprisonment', 'punishment', 'life'],
            'jail': ['imprisonment', 'punishment'],
            'harm': ['attempt', 'assault', 'injury'],
            'injure': ['attempt', 'assault', 'injury'],
            'negligence': ['negligence', 'accident'],
            'accident': ['negligence', 'accident'],
            'rash': ['negligence', 'rash'],
            'article 19': ['constitutional', 'fundamental rights'],
            'article 21': ['constitutional', 'life', 'death'],
            'freedom': ['constitutional', 'fundamental rights'],
            'rights': ['constitutional', 'fundamental rights'],
        }
        
        for keyword, related_topics in keyword_map.items():
            if keyword in query_lower:
                topics.extend(related_topics)
        
        # Default topics if nothing found
        if not topics:
            topics = ['general', 'indian law']
        
        return list(set(topics))  # Remove duplicates
