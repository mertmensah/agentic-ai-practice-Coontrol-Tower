"""
Content Moderation Agent - Agent 1
Checks if text is workplace appropriate using Google Gemini
"""
from typing import Dict, Any
from .simple_agent import BaseAgent

class ContentModeratorAgent(BaseAgent):
    """
    Agent that evaluates if text content is workplace appropriate
    Powered by Google Gemini
    """
    
    def __init__(self):
        system_prompt = """You are a professional content moderator for workplace communications.
Your job is to analyze text and determine if it is appropriate for a professional workplace environment.

Evaluate the text based on:
1. Profanity or offensive language
2. Discriminatory content (race, gender, religion, etc.)
3. Sexual content or harassment
4. Threats or violence
5. Confidential or sensitive information risks

Respond ONLY in this JSON format:
{
    "appropriate": true/false,
    "reason": "Brief explanation of your decision",
    "severity": "none/low/medium/high",
    "suggestions": "Optional suggestions for improvement if inappropriate"
}

Be strict but fair in your evaluation."""

        super().__init__(
            system_prompt=system_prompt,
            agent_type="ContentModeratorAgent"
        )
        
    def process(self, input_text: str) -> Dict[str, Any]:
        """
        Check if text is workplace appropriate using Google Gemini
        
        Args:
            input_text: Text to evaluate
            
        Returns:
            Dictionary with moderation results
        """
        if not input_text or not input_text.strip():
            return {
                "appropriate": False,
                "reason": "Empty input provided",
                "severity": "none",
                "original_text": input_text
            }
        
        # Call Gemini with moderation prompt
        response = self.call_gemini(
            user_message=f"Evaluate this text for workplace appropriateness:\n\n\"{input_text}\"",
            temperature=0.3  # Lower temperature for more consistent moderation
        )
        
        # Parse response (in production, use proper JSON parsing with error handling)
        result = {
            "agent": self.agent_type,
            "original_text": input_text,
            "analysis": response,
            "status": "analyzed"
        }
        
        return result
