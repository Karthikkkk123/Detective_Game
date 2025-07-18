import re
from difflib import SequenceMatcher
from typing import Dict, List, Optional

class TextProcessor:
    def __init__(self):
        self.question_patterns = {
            'weapon': ['weapon', 'gun', 'knife', 'pistol', 'sword', 'tool', 'murder weapon'],
            'victim': ['victim', 'dead', 'body', 'corpse', 'deceased', 'killed'],
            'suspects': ['suspect', 'suspects', 'who', 'person', 'people', 'accused'],
            'location': ['where', 'location', 'place', 'scene', 'room', 'house'],
            'time': ['when', 'time', 'hour', 'morning', 'evening', 'night', 'day'],
            'motive': ['why', 'motive', 'reason', 'cause', 'purpose'],
            'evidence': ['evidence', 'clue', 'proof', 'fingerprint', 'dna', 'blood'],
            'alibi': ['alibi', 'whereabouts', 'where was', 'doing'],
            'relationship': ['relationship', 'related', 'family', 'friend', 'enemy']
        }
    
    def process_question(self, question: str, case_data: Dict) -> Optional[str]:
        """Process user question and return relevant response"""
        question_lower = question.lower()
        
        # Extract question type using pattern matching
        question_type = self._identify_question_type(question_lower)
        
        if not question_type:
            return None
        
        # Get relevant information from case data
        return self._get_response(question_type, question_lower, case_data)
    
    def _identify_question_type(self, question: str) -> Optional[str]:
        """Identify the type of question being asked"""
        best_match = None
        best_score = 0
        
        for q_type, patterns in self.question_patterns.items():
            for pattern in patterns:
                if pattern in question:
                    # Calculate similarity score
                    score = SequenceMatcher(None, pattern, question).ratio()
                    if score > best_score:
                        best_score = score
                        best_match = q_type
        
        return best_match if best_score > 0.1 else None
    
    def _get_response(self, question_type: str, question: str, case_data: Dict) -> Optional[str]:
        """Get appropriate response based on question type"""
        
        if question_type == 'weapon':
            return case_data.get('weapon', {}).get('description', 'The murder weapon has not been determined.')
        
        elif question_type == 'victim':
            victim = case_data.get('victim', {})
            return f"The victim is {victim.get('name', 'unknown')}. {victim.get('description', '')}"
        
        elif question_type == 'suspects':
            suspects = case_data.get('suspects', [])
            if suspects:
                names = [s['name'] for s in suspects]
                return f"The suspects are: {', '.join(names)}"
            return "No suspects have been identified yet."
        
        elif question_type == 'location':
            location = case_data.get('location', 'Unknown location')
            scene_description = case_data.get('scene_description', '')
            return f"The crime occurred at {location}. {scene_description}"
        
        elif question_type == 'time':
            time_info = case_data.get('time_of_death', 'Time of death is unknown')
            return f"Time of death: {time_info}"
        
        elif question_type == 'motive':
            return case_data.get('motive_hint', 'The motive is still unclear.')
        
        elif question_type == 'evidence':
            evidence = case_data.get('evidence', [])
            if evidence:
                return f"Evidence found: {', '.join(evidence)}"
            return "No evidence has been found yet."
        
        elif question_type == 'alibi':
            # Extract suspect name from question
            suspect_name = self._extract_suspect_name(question, case_data)
            if suspect_name:
                suspect = self._find_suspect(suspect_name, case_data)
                if suspect:
                    return suspect.get('alibi', f"{suspect_name}'s alibi is unknown.")
            return "Please specify which suspect's alibi you're asking about."
        
        elif question_type == 'relationship':
            # Extract suspect name from question
            suspect_name = self._extract_suspect_name(question, case_data)
            if suspect_name:
                suspect = self._find_suspect(suspect_name, case_data)
                if suspect:
                    return suspect.get('relationship', f"{suspect_name}'s relationship to the victim is unknown.")
            return "Please specify which suspect's relationship you're asking about."
        
        return None
    
    def _extract_suspect_name(self, question: str, case_data: Dict) -> Optional[str]:
        """Extract suspect name from question"""
        suspects = case_data.get('suspects', [])
        
        for suspect in suspects:
            name = suspect['name'].lower()
            first_name = name.split()[0] if name.split() else name
            
            if name in question or first_name in question:
                return suspect['name']
        
        return None
    
    def _find_suspect(self, suspect_name: str, case_data: Dict) -> Optional[Dict]:
        """Find suspect in case data"""
        suspects = case_data.get('suspects', [])
        
        for suspect in suspects:
            if suspect['name'].lower() == suspect_name.lower():
                return suspect
        
        return None
