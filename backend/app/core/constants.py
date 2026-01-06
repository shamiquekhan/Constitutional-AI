"""
Constants used throughout the application
"""

# Document Types
DOCUMENT_TYPES = {
    "CONSTITUTION": "constitution",
    "STATUTE": "statute",
    "CASE_LAW": "case_law",
    "HIGH_COURT": "high_court",
    "SUPREME_COURT": "supreme_court",
}

# Authority Levels
AUTHORITY_LEVELS = {
    "SUPREME": "supreme",
    "HIGH": "high",
    "STATUTE": "statute",
    "REGULATION": "regulation",
}

# Citation Status
CITATION_STATUS = {
    "ACTIVE": "active",
    "AMENDED": "amended",
    "REPEALED": "repealed",
    "UNDER_REVIEW": "under_review",
}

# Jurisdictions
JURISDICTIONS = [
    "all_india",
    "delhi",
    "mumbai",
    "kolkata",
    "chennai",
    "bangalore",
    "hyderabad",
]

# Legal Codes
LEGAL_CODES = {
    "CONSTITUTION": "Constitution of India",
    "IPC": "Indian Penal Code",
    "CRPC": "Code of Criminal Procedure",
    "CPC": "Civil Procedure Code",
    "CONTRACT_ACT": "Indian Contract Act",
    "EVIDENCE_ACT": "Indian Evidence Act",
}

# Confidence Thresholds
CONFIDENCE_THRESHOLDS = {
    "HIGH": 0.85,
    "MEDIUM": 0.65,
    "LOW": 0.45,
}

# System Prompts
SYSTEM_PROMPTS = {
    "LEGAL_QA": """You are a legal AI assistant specializing in Indian law. You MUST:
1. Only use the provided legal sources in your response
2. Include explicit citations in [Citation: <source>] format for every claim
3. Say "I don't have verified sources for this" if insufficient data is available
4. Never make up cases, sections, or legal interpretations
5. Show confidence level based on source quality and quantity
6. Use professional legal language
7. Be precise and accurate - in law, details matter

Remember: In law, creativity is dangerous. Speak only when you have proof.""",
    
    "DEVILS_ADVOCATE": """You are a legal AI assistant tasked with finding opposing arguments.
Given a legal position, you must:
1. Identify weak points in the argument
2. Find contradictory precedents or interpretations
3. Present the strongest counter-arguments
4. Cite sources for opposing views
5. Be objective and thorough

Your goal is to help prepare for opposition arguments.""",
    
    "MEMORANDUM": """You are a legal AI assistant generating a formal legal memorandum.
Follow the IRAC structure:
- Issue: State the legal question clearly
- Rule: Cite relevant laws and precedents
- Application: Apply law to facts
- Conclusion: Provide legal conclusion

Ensure all citations are verified and properly formatted."""
}

# Error Messages
ERROR_MESSAGES = {
    "NO_SOURCES": "I don't have sufficient verified sources to answer this question accurately.",
    "VERIFICATION_FAILED": "Citation verification failed. Please try again.",
    "QUERY_TOO_SHORT": "Query must be at least 3 characters long.",
    "QUERY_TOO_LONG": "Query exceeds maximum length of 1000 characters.",
    "INVALID_JURISDICTION": "Invalid jurisdiction specified.",
}
