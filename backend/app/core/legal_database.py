"""
Legal Database - Comprehensive Indian Law Sources
Contains IPC, CrPC, Constitution, and Supreme Court judgments
"""

from enum import Enum
from typing import List, Dict


class LegalSourceType(Enum):
    CONSTITUTION = "constitution"
    IPC = "ipc"
    CRPC = "crpc"
    STATUTE = "statute"
    CASE_LAW = "case_law"
    JUDGMENT = "judgment"


class LegalDatabase:
    """
    Database of laws, sections, and case laws for Indian legal system
    """
    
    def __init__(self):
        self.sources = {
            # ===== MURDER - Section 302 IPC =====
            'Section 302 IPC': {
                'type': LegalSourceType.IPC,
                'title': 'Punishment for murder',
                'text': '''Section 302 IPC: "Whoever commits murder shall be punished with death, or with life imprisonment, and shall also be liable to fine."

Key Points:
• Applicable when death is caused with intention to cause death
• Maximum punishment: Death penalty
• Alternative: Life imprisonment + fine
• Minimum punishment: Life imprisonment (as per Bachan Singh v. State of Punjab)
• Death penalty only in "rarest of rare cases"
''',
                'relevant_to': ['murder', 'killing', 'death', 'punishment', 'life']
            },
            
            # ===== DEATH BY NEGLIGENCE - Section 304 IPC =====
            'Section 304 IPC': {
                'type': LegalSourceType.IPC,
                'title': 'Culpable homicide not amounting to murder',
                'text': '''Section 304 IPC: Culpable homicide not amounting to murder

Part I: If done with knowledge that likely to cause death - 
Punishment: Life imprisonment or imprisonment up to 10 years + fine

Part II: If done with knowledge likely to cause death but without intention -
Punishment: Imprisonment up to 10 years or fine or both

Distinction from Murder (Section 302):
• 302: Intention to cause death
• 304: Knowledge death may result, but no intention

Example: Death in sudden fight without premeditation
''',
                'relevant_to': ['negligence', 'accident', 'death', 'rash', 'killing', 'punishment']
            },
            
            # ===== ATTEMPT TO MURDER - Section 307 IPC =====
            'Section 307 IPC': {
                'type': LegalSourceType.IPC,
                'title': 'Attempt to murder',
                'text': '''Section 307 IPC: "Whoever does any act with such intention or knowledge, and under such circumstances that, if he by that act caused death, he would be guilty of murder, shall be punished with imprisonment of either description for a term which may extend to ten years, and shall also be liable to fine."

Key Points:
• Does not require actual death
• Only attempt with intention to cause death
• Punishment: Up to 10 years imprisonment + fine
• If hurt caused: May extend to life imprisonment
• Serious bodily injury: Additional charges under Section 325, 326 possible
''',
                'relevant_to': ['attempt', 'murder', 'harm', 'injury', 'punishment']
            },
            
            # ===== RIGHT TO LIFE - Article 21 =====
            'Article 21 Constitution': {
                'type': LegalSourceType.CONSTITUTION,
                'title': 'Protection of life and personal liberty',
                'text': '''Article 21 Constitution of India: "No person shall be deprived of his life or personal liberty except according to procedure established by law."

Scope:
• Right to life includes right to live with human dignity
• Every person has inherent right to life
• State can only deprive life through due legal procedure
• Court scrutinizes death sentences with utmost care
• Includes right to livelihood, shelter, health

Landmark Interpretations:
• Maneka Gandhi v. Union of India (1978): Procedure must be just, fair and reasonable
• Francis Coralie Mullin v. UT of Delhi (1981): Right to life includes right to human dignity
''',
                'relevant_to': ['life', 'death', 'punishment', 'constitutional', 'fundamental rights']
            },
            
            # ===== FUNDAMENTAL RIGHTS - Article 19 =====
            'Article 19 Constitution': {
                'type': LegalSourceType.CONSTITUTION,
                'title': 'Protection of certain rights regarding freedom of speech etc.',
                'text': '''Article 19(1) Constitution of India: All citizens shall have the right to:

(a) freedom of speech and expression
(b) assemble peacefully and without arms
(c) form associations or unions
(d) move freely throughout the territory of India
(e) reside and settle in any part of India
(f) practice any profession, or to carry on any occupation, trade or business

Article 19(2): Reasonable restrictions on freedom of speech in interests of:
• Sovereignty and integrity of India
• Security of State
• Friendly relations with foreign States
• Public order, decency or morality
• Contempt of court
• Defamation
• Incitement to offence

Examples:
• You CAN criticize government policies
• You CAN protest peacefully
• You CANNOT incite violence
• You CANNOT defame individuals
''',
                'relevant_to': ['constitutional', 'fundamental rights', 'freedom', 'speech']
            },
            
            # ===== SENTENCING GUIDELINES =====
            'Bachan Singh v. State of Punjab (1980)': {
                'type': LegalSourceType.JUDGMENT,
                'court': 'Supreme Court',
                'year': 1980,
                'citation': '(1980) 2 SCC 684',
                'title': 'Guidelines for imposing death sentence - Rarest of Rare Doctrine',
                'text': '''Bachan Singh v. State of Punjab, (1980) 2 SCC 684

LANDMARK JUDGMENT establishing "RAREST OF RARE CASES DOCTRINE":

1. Principle:
   • Death penalty only for rarest of rare cases
   • Not the norm, but an exception
   • Life imprisonment is the rule
   
2. Sentencing Principles:
   • Gravity and brutality of crime
   • Nature of offense
   • Character and antecedents of criminal
   • Circumstances of the case
   • Possibility of reformation
   
3. Procedural Safeguards:
   • Separate hearing for sentencing after conviction
   • Aggravating vs. mitigating factors must be considered
   • Two separate judgments (guilt phase + sentencing phase)
   
4. Examples of Rarest of Rare Cases:
   • Heinous crimes with extreme brutality
   • Murder with premeditation and cruelty
   • Multiple murders
   • Murder of public figures/law enforcement
   • Terrorist activities causing mass casualties
   
PRACTICAL IMPACT:
• If death penalty not given, minimum is life imprisonment
• Life imprisonment typically means 14-20 years actual jail time before parole eligibility
''',
                'relevant_to': ['murder', 'punishment', 'death', 'sentencing', 'life']
            },
            
            # ===== LIFE IMPRISONMENT GUIDELINES =====
            'Mulla v. State of Maharashtra (2013)': {
                'type': LegalSourceType.JUDGMENT,
                'court': 'Supreme Court',
                'year': 2013,
                'citation': '(2013) 15 SCC 497',
                'title': 'Meaning and duration of life imprisonment',
                'text': '''Mulla v. State of Maharashtra, (2013) 15 SCC 497

CLARIFICATIONS on Life Imprisonment:

1. Duration:
   • Life imprisonment = imprisonment for natural life
   • NOT a fixed period (not 14 years or 20 years)
   • Average actual imprisonment: 20-25 years
   
2. Remission and Release:
   • State Government can grant remission under Section 432 CrPC
   • Life convict eligible for release consideration after 14 years
   • Subject to State remission policy
   • Prison Conduct Rules apply
   
3. Conditions for Release:
   • Good conduct in prison
   • Assessment by prison authorities
   • Superintendent's recommendation
   • Release is discretionary, not automatic
   
4. Special Provisions:
   • Courts can impose "life imprisonment without remission"
   • Courts can specify minimum imprisonment period (e.g., "30 years without remission")
   
PRACTICAL OUTCOME:
Life imprisonment for murder typically means:
• 14-20 years actual jail time
• Then eligibility for parole/release
• Subject to good behavior and state policy
• Some states more liberal, others more strict
''',
                'relevant_to': ['life', 'imprisonment', 'punishment', 'release', 'jail']
            },
        }
    
    def get_relevant_sources(self, query_topics: List[str]) -> List[Dict]:
        """Get all relevant legal sources for query topics"""
        
        relevant = []
        seen_sources = set()
        
        for source_name, source_data in self.sources.items():
            # Check if source is relevant to query topics
            source_topics = source_data.get('relevant_to', [])
            
            for topic in query_topics:
                topic_lower = topic.lower()
                if topic_lower in [t.lower() for t in source_topics]:
                    if source_name not in seen_sources:
                        relevant.append({
                            'source': source_name,
                            'type': source_data['type'].value,
                            'title': source_data.get('title', ''),
                            'text': source_data.get('text', ''),
                            'year': source_data.get('year', None),
                            'court': source_data.get('court', None),
                            'citation': source_data.get('citation', None)
                        })
                        seen_sources.add(source_name)
                    break
        
        # If no sources found, return general legal framework
        if not relevant:
            # Return Article 21 as default
            default_source = self.sources.get('Article 21 Constitution')
            if default_source:
                relevant.append({
                    'source': 'Article 21 Constitution',
                    'type': default_source['type'].value,
                    'title': default_source.get('title', ''),
                    'text': default_source.get('text', ''),
                })
        
        return relevant
