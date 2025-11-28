"""
Cat Breed Matching Agent
Identifies and suggests cat breeds based on descriptions or images
"""
from typing import Dict, Any
from .simple_agent import BaseAgent

class BreedMatchAgent(BaseAgent):
    """
    Agent that identifies cat breeds and provides breed information
    Powered by Google Gemini
    """
    
    def __init__(self):
        system_prompt = """You are an expert cat breed identifier and feline geneticist! 🐱

Your job is to analyze descriptions or characteristics and identify the most likely cat breed(s).

Provide detailed information including:
1. Most likely breed name
2. Key characteristics that match
3. Confidence level (high/medium/low)
4. Brief description of the breed
5. Personality traits
6. Care requirements

Be knowledgeable about:
- Recognized cat breeds (Persian, Maine Coon, Siamese, British Shorthair, etc.)
- Mixed breeds and common combinations
- Physical characteristics (coat, eyes, size, build)
- Personality traits associated with breeds

Format your response as:
**Breed**: [Name]
**Confidence**: [High/Medium/Low]
**Match Reasons**: [Why this breed matches]
**Description**: [Brief breed description]
**Personality**: [Typical temperament]
**Care Notes**: [Special care requirements]

Be friendly and informative!"""

        super().__init__(
            system_prompt=system_prompt,
            agent_type="BreedMatchAgent"
        )
        
    def process(self, input_text: str) -> Dict[str, Any]:
        """
        Match cat breed based on description
        
        Args:
            input_text: Description of cat characteristics
            
        Returns:
            Dictionary with breed matching results
        """
        if not input_text or not input_text.strip():
            return {
                "breed": "Unknown",
                "confidence": "low",
                "analysis": "No description provided",
                "agent": self.agent_type,
                "status": "analyzed"
            }
        
        # Call Gemini with breed matching prompt
        response = self.call_gemini(
            user_message=f"Identify the cat breed based on this description:\n\n\"{input_text}\"",
            temperature=0.4  # Moderate temperature for accurate breed identification
        )
        
        result = {
            "agent": self.agent_type,
            "input": input_text,
            "breed_analysis": response,
            "status": "analyzed"
        }
        
        return result
