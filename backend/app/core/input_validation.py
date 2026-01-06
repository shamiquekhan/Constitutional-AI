"""
Input Validation Layer for Constitutional AI
Prevents harmful queries from reaching RAG pipeline
"""

import re
from typing import Tuple, Dict
import logging

logger = logging.getLogger(__name__)


class InputValidator:
    """
    Validates user queries before processing
    Prevents harmful queries from reaching RAG pipeline
    """
    
    def __init__(self):
        # Harmful intent keywords
        self.harmful_patterns = [
            r'\b(kill|murder|harm|hurt|injure|assault|beat|stab|shoot|poison)\b',
            r'\b(illegal|unlawful)\s+(activity|action|thing|way)',
            r'\bcan\s+i\s+(kill|harm|poison|murder|hurt)',
            r'\bhow\s+to\s+(kill|poison|harm|murder)',
            r'\bways?\s+to\s+(kill|harm|injure|murder)',
            r'\b(commit|do)\s+(crime|murder|assault)',
        ]
        
        # Personal advice patterns (require lawyer consultation)
        self.personal_advice_patterns = [
            r'\b(my|i\s+(am|am\s+facing|have|will|did))',
            r'\bwill\s+i\s+(get|be|face|go\s+to)',
            r'\bam\s+i\s+(liable|guilty|responsible|in\s+trouble)',
            r'\bcan\s+i\s+(do|say|challenge|file)',
            r'\bshould\s+i\s+(do|say|file|hire)',
            r'\bwhat\s+if\s+i\s+(did|do|said)',
        ]
        
        # Scope validation patterns (only Indian law)
        self.invalid_jurisdiction = [
            r'\b(us|usa|american|british|uk|australian|chinese|canadian)\s+(law|court|constitution)',
            r'\b(dui|felony|misdemeanor)\b',
            r'\b(copyright|patent|trademark)\s+(law|infringement)',
        ]
        
        self.min_query_length = 5
        self.max_query_length = 500
    
    def validate_query(self, query: str) -> Tuple[bool, str, Dict]:
        """
        Comprehensive query validation
        Returns: (is_valid, reason, metadata)
        """
        
        validation_result = {
            'is_valid': True,
            'validation_type': 'pass',
            'reason': '',
            'should_refuse': False,
            'requires_lawyer': False,
            'is_harmful': False,
            'is_personal_advice': False,
            'confidence_penalty': 0.0
        }
        
        # Check 1: Length validation
        if len(query.strip()) < self.min_query_length:
            validation_result['is_valid'] = False
            validation_result['reason'] = 'Query too short (minimum 5 characters)'
            return False, validation_result['reason'], validation_result
        
        if len(query) > self.max_query_length:
            validation_result['is_valid'] = False
            validation_result['reason'] = 'Query too long (maximum 500 characters)'
            return False, validation_result['reason'], validation_result
        
        query_lower = query.lower()
        
        # Check 2: HARMFUL INTENT DETECTION
        for pattern in self.harmful_patterns:
            if re.search(pattern, query_lower, re.IGNORECASE):
                validation_result['is_valid'] = False
                validation_result['is_harmful'] = True
                validation_result['should_refuse'] = True
                validation_result['reason'] = (
                    'This query appears to be asking for legal advice about harmful activities. '
                    'I cannot provide guidance on illegal or harmful actions. '
                    'Please consult a qualified lawyer if you need legal assistance.'
                )
                logger.warning(f"Harmful query detected: {query[:50]}...")
                return False, validation_result['reason'], validation_result
        
        # Check 3: PERSONAL ADVICE DETECTION
        for pattern in self.personal_advice_patterns:
            if re.search(pattern, query_lower):
                validation_result['is_personal_advice'] = True
                validation_result['requires_lawyer'] = True
                validation_result['confidence_penalty'] = 0.30  # Reduce confidence by 30%
                logger.info(f"Personal advice query detected: {query[:50]}...")
                break
        
        # Check 4: JURISDICTION CHECK
        for pattern in self.invalid_jurisdiction:
            if re.search(pattern, query_lower):
                validation_result['is_valid'] = False
                validation_result['should_refuse'] = True
                validation_result['reason'] = (
                    'This question appears to be about non-Indian law. '
                    'I specialize in Indian Constitutional and criminal law. '
                    'Please ask about Indian law.'
                )
                logger.info(f"Non-Indian jurisdiction detected: {query[:50]}...")
                return False, validation_result['reason'], validation_result
        
        # Check 5: EMPTY/SPAM CHECK
        if not query.strip():
            validation_result['is_valid'] = False
            validation_result['reason'] = 'Query cannot be empty'
            return False, validation_result['reason'], validation_result
        
        # Check 6: Excessive whitespace (potential spam)
        word_count = len(query.split())
        if word_count > 100:
            validation_result['is_valid'] = False
            validation_result['reason'] = 'Query too long (maximum 100 words)'
            return False, validation_result['reason'], validation_result
        
        return True, 'Query passed validation', validation_result
