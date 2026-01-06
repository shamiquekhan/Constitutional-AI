"""
Services Module
"""

from app.services.legal_qa import LegalQAService
from app.services.verification_service import VerificationService

__all__ = [
    'LegalQAService',
    'VerificationService'
]
