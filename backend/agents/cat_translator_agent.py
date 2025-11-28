"""
Cat Language Translator Agent - Agent 2
Converts text to cat language (meows) using Google Gemini
"""
from typing import Dict, Any
from .simple_agent import BaseAgent

class CatTranslatorAgent(BaseAgent):
    """
    Agent that translates text into cat language (meows)
    Powered by Google Gemini
    """
    
    def __init__(self):
        system_prompt = """You are a creative cat language translator! 🐱

Your job is to convert human text into cat language using meows, purrs, and cat expressions.

Rules for translation:
1. Use variations of "meow", "mrow", "purr", "mrrp", "nya" 
2. Match the emotion and tone of the original text
3. Use capitalization for emphasis (MEOW for shouting, meow for normal)
4. Add cat emojis for extra expression (😺, 😸, 😹, 😻, 😼, 😽, 😾, 😿, 🙀)
5. Preserve the general length and structure
6. Make it fun and playful!

Examples:
- "Hello, how are you?" → "Meow meow, mrow mrow? 😺"
- "I'm so excited!" → "MEOW MEOW MEOW! 😻"
- "I'm sad today" → "mrow... purr... 😿"
- "Thank you very much" → "Mrrp mrrp purr purr 😸"

Be creative and cat-like in your translations!"""

        super().__init__(
            system_prompt=system_prompt,
            agent_type="CatTranslatorAgent"
        )
        
    def process(self, input_text: str) -> Dict[str, Any]:
        """
        Translate text to cat language using Google Gemini
        
        Args:
            input_text: Text to translate
            
        Returns:
            Dictionary with translation results
        """
        if not input_text or not input_text.strip():
            return {
                "original_text": input_text,
                "cat_translation": "Mrow? 😿 (Empty input detected)",
                "agent": self.agent_type,
                "status": "translated"
            }
        
        # Call Gemini with translation prompt
        cat_text = self.call_gemini(
            user_message=f"Translate this to cat language:\n\n\"{input_text}\"",
            temperature=0.9  # Higher temperature for more creative translations
        )
        
        result = {
            "agent": self.agent_type,
            "original_text": input_text,
            "cat_translation": cat_text,
            "status": "translated"
        }
        
        return result
