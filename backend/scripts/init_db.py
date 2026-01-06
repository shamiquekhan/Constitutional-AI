"""
Database Initialization Script
Creates all database tables
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database.session import engine, Base
from app.database.models import QueryHistory, CitationStatus, LegalDocument, User
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_database():
    """
    Create all database tables
    """
    try:
        logger.info("Creating database tables...")
        Base.metadata.create_all(bind=engine)
        logger.info("✓ Database tables created successfully")
        
        # List created tables
        logger.info("Tables created:")
        for table in Base.metadata.sorted_tables:
            logger.info(f"  - {table.name}")
    
    except Exception as e:
        logger.error(f"Error creating database tables: {e}")
        raise

if __name__ == "__main__":
    init_database()
