"""
Document Seeding Script
Ingests legal documents into the knowledge base
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import logging
from app.database.session import SessionLocal
from app.database.models import LegalDocument

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def seed_mock_documents():
    """
    Seed database with mock legal documents for testing
    
    In production, this would:
    1. Parse PDF legal documents
    2. Chunk text semantically
    3. Generate embeddings
    4. Index in Pinecone
    5. Store metadata in PostgreSQL
    """
    
    db = SessionLocal()
    
    mock_documents = [
        {
            "document_id": "const-art-19",
            "title": "Constitution of India - Article 19",
            "source": "Constitution of India",
            "section": "Article 19",
            "content": """Article 19: Protection of certain rights regarding freedom of speech, etc.
            
(1) All citizens shall have the right—
(a) to freedom of speech and expression;
(b) to assemble peaceably and without arms;
(c) to form associations or unions;
(d) to move freely throughout the territory of India;
(e) to reside and settle in any part of the territory of India; and
(f) omitted
(g) to practise any profession, or to carry on any occupation, trade or business.
            
(2) Nothing in sub-clause (a) of clause (1) shall affect the operation of any existing law...""",
            "authority_level": "supreme",
            "jurisdiction": "all_india",
            "code_type": "constitution",
            "effective_date": "1950-01-26",
            "metadata": {
                "amendments": ["44th Amendment - 1978"],
                "related_articles": ["Article 14", "Article 21"]
            }
        },
        {
            "document_id": "ipc-sec-302",
            "title": "Indian Penal Code - Section 302",
            "source": "Indian Penal Code",
            "section": "Section 302",
            "content": """Section 302: Punishment for murder
            
Whoever commits murder shall be punished with death, or imprisonment for life, and shall also be liable to fine.""",
            "authority_level": "statute",
            "jurisdiction": "all_india",
            "code_type": "ipc",
            "effective_date": "1860-01-01",
            "metadata": {
                "chapter": "XVI - Of Offences Affecting the Human Body",
                "related_sections": ["Section 300", "Section 304"]
            }
        }
    ]
    
    try:
        for doc_data in mock_documents:
            # Check if document already exists
            existing = db.query(LegalDocument).filter(
                LegalDocument.document_id == doc_data["document_id"]
            ).first()
            
            if not existing:
                document = LegalDocument(**doc_data)
                db.add(document)
                logger.info(f"Added document: {doc_data['title']}")
            else:
                logger.info(f"Document already exists: {doc_data['title']}")
        
        db.commit()
        logger.info("✓ Knowledge base seeded successfully")
    
    except Exception as e:
        logger.error(f"Error seeding database: {e}")
        db.rollback()
    
    finally:
        db.close()

if __name__ == "__main__":
    logger.info("Starting knowledge base seeding...")
    seed_mock_documents()
    logger.info("Done!")
