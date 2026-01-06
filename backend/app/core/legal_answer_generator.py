"""
Legal Answer Generator - Creates comprehensive answers with proper citations
"""

from typing import Dict, List
from app.core.legal_database import LegalDatabase


class LegalAnswerGenerator:
    """Generates comprehensive legal answers with proper citations"""
    
    def __init__(self):
        self.database = LegalDatabase()
    
    def generate_answer(self, query: str, topics: List[str]) -> Dict:
        """
        Generate comprehensive answer with all citations
        Returns: Dict with answer text, sources, and metadata
        """
        
        # Get relevant sources
        sources = self.database.get_relevant_sources(topics)
        
        if not sources:
            return self._generate_no_sources_answer(query)
        
        # Build comprehensive answer
        answer_parts = []
        
        # Add topic-specific introduction
        intro = self._generate_introduction(query, topics)
        answer_parts.append(intro)
        
        # Add divider
        answer_parts.append("\n" + "═" * 80 + "\n")
        
        # Add each relevant source with proper formatting
        for i, source in enumerate(sources, 1):
            answer_parts.append(self._format_source(i, source))
            answer_parts.append("\n" + "-" * 80 + "\n")
        
        # Add summary section
        summary = self._generate_summary(sources, topics)
        answer_parts.append(summary)
        
        # Calculate confidence based on source quality
        confidence = self._calculate_confidence(sources)
        
        return {
            'answer': '\n'.join(answer_parts),
            'sources': sources,
            'confidence': confidence,
            'has_case_laws': any(s['type'] in ['judgment', 'case_law'] for s in sources),
            'has_constitutional': any(s['type'] == 'constitution' for s in sources),
            'has_ipc': any(s['type'] == 'ipc' for s in sources),
            'num_sources': len(sources)
        }
    
    def _generate_introduction(self, query: str, topics: List[str]) -> str:
        """Generate contextual introduction based on query topics"""
        
        if 'murder' in topics or 'killing' in topics:
            return '''LEGAL CONSEQUENCES OF CAUSING DEATH TO ANOTHER PERSON
(Under Indian Penal Code, Constitution of India, and Supreme Court Precedents)

The legal consequences of causing death to another person depend on:
1. INTENTION: Whether death was intended or accidental
2. CIRCUMSTANCES: Premeditated vs sudden provocation
3. NATURE: Murder vs culpable homicide vs negligence

The following authorities apply:'''
        
        elif 'fundamental rights' in topics or 'freedom' in topics:
            return '''FUNDAMENTAL RIGHTS UNDER INDIAN CONSTITUTION

The Constitution of India guarantees fundamental rights to all citizens under Part III (Articles 12-35). These rights are enforceable through courts and form the foundation of Indian democracy.

The following constitutional provisions apply:'''
        
        else:
            return '''LEGAL FRAMEWORK UNDER INDIAN LAW

Based on your query, the following legal authorities are relevant:'''
    
    def _format_source(self, num: int, source: Dict) -> str:
        """Format a legal source with proper structure"""
        
        parts = []
        
        # Header
        parts.append(f"\n{num}. {source['source'].upper()}")
        
        # Court and year for judgments
        if source.get('court') and source.get('year'):
            citation = source.get('citation', '')
            parts.append(f"   {source['court']}, {source['year']}")
            if citation:
                parts.append(f"   Citation: {citation}")
        
        # Title
        parts.append(f"\n   {source['title']}")
        
        # Content
        parts.append(f"\n{source['text']}")
        
        return '\n'.join(parts)
    
    def _generate_summary(self, sources: List[Dict], topics: List[str]) -> str:
        """Generate summary section based on sources"""
        
        summary_parts = []
        summary_parts.append("\n" + "═" * 80)
        summary_parts.append("\nSUMMARY")
        summary_parts.append("\n" + "═" * 80 + "\n")
        
        # Murder-specific summary
        if any('murder' in s['relevant_to'] if 'relevant_to' in str(s) else False for s in sources):
            summary_parts.append('''
PUNISHMENTS FOR CAUSING DEATH:

1. MURDER (Section 302 IPC)
   • Intention to cause death
   • Punishment: DEATH or LIFE IMPRISONMENT + Fine
   • Death penalty only in "rarest of rare cases"
   • Life imprisonment typically 14-20 years actual jail time

2. CULPABLE HOMICIDE (Section 304 IPC)
   • Knowledge death may result, but no intention
   • Punishment: Up to 10 years imprisonment + fine
   • Examples: Death in sudden fight, unplanned killing

3. ATTEMPT TO MURDER (Section 307 IPC)
   • Any act with intention to cause death (no actual death required)
   • Punishment: Up to 10 years imprisonment + fine
   • If hurt caused: May extend to life imprisonment

4. CONSTITUTIONAL PROTECTION (Article 21)
   • Right to life guaranteed to all
   • State can deprive life only through due legal process
   • Death sentences subject to highest judicial scrutiny
''')
        
        # Add procedural information
        if 'murder' in topics or 'punishment' in topics:
            summary_parts.append('''
LEGAL PROCEDURE:

1. INVESTIGATION (2-6 months):
   • Police file FIR under relevant IPC sections
   • Evidence collection and witness statements
   
2. TRIAL (2-5 years average):
   • District Court or Sessions Court
   • Prosecution presents evidence
   • Defense cross-examination
   
3. JUDGMENT:
   • Guilty or Not Guilty verdict
   • If guilty: Separate sentencing hearing
   • Consideration of aggravating and mitigating factors
   
4. APPEALS:
   • High Court review (mandatory in death penalty cases)
   • Supreme Court review (if High Court upholds death)
   • Presidential mercy petition (in death cases)

TOTAL TIMELINE: 5-10+ years from crime to final judgment
''')
        
        # Citations summary
        summary_parts.append(f"\nSOURCES CITED: {len(sources)}")
        for source in sources:
            summary_parts.append(f"   • {source['source']}")
        
        summary_parts.append("\n" + "═" * 80)
        summary_parts.append('''
IMPORTANT DISCLAIMER:
This answer is for educational purposes only. For specific legal advice regarding your situation, please consult a qualified lawyer admitted to practice in India.
''')
        
        return '\n'.join(summary_parts)
    
    def _calculate_confidence(self, sources: List[Dict]) -> float:
        """Calculate confidence score based on source quality"""
        
        if not sources:
            return 0.3
        
        confidence = 0.5  # Base confidence
        
        # Increase confidence for quality indicators
        if len(sources) >= 3:
            confidence += 0.2
        elif len(sources) >= 2:
            confidence += 0.1
        
        # Supreme Court judgments increase confidence
        if any(s.get('court') == 'Supreme Court' for s in sources):
            confidence += 0.15
        
        # Constitutional provisions increase confidence
        if any(s['type'] == 'constitution' for s in sources):
            confidence += 0.1
        
        # IPC sections increase confidence
        if any(s['type'] == 'ipc' for s in sources):
            confidence += 0.05
        
        return min(confidence, 0.95)  # Cap at 95%
    
    def _generate_no_sources_answer(self, query: str) -> Dict:
        """Generate response when no sources are found"""
        
        return {
            'answer': '''I apologize, but I could not find specific legal sources to answer your query in my current database.

My knowledge base focuses on:
• Indian Penal Code (IPC)
• Criminal Procedure Code (CrPC)
• Constitution of India
• Supreme Court and High Court judgments
• Major statutory provisions

For comprehensive legal research on your specific query, I recommend:
1. Consulting a qualified lawyer
2. Visiting a law library
3. Accessing legal databases like SCC Online, Manupatra, or Indian Kanoon

If you have questions about criminal law, constitutional rights, or major legal procedures, please rephrase your query and I'll do my best to help.''',
            'sources': [],
            'confidence': 0.0,
            'has_case_laws': False,
            'has_constitutional': False,
            'has_ipc': False,
            'num_sources': 0
        }
