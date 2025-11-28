"""
Base Agent Class - Foundation for all specialized agents
Uses Google Gemini API
"""
import google.generativeai as genai
from typing import Dict, Any, Optional
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import GEMINI_API_KEY, GEMINI_MODEL

class BaseAgent:
    """
    Base class for all AI agents using Google Gemini API
    """
    
    def __init__(self, system_prompt: str, agent_type: str):
        """
        Initialize the base agent with Google Gemini
        
        Args:
            system_prompt: The system message that defines agent behavior
            agent_type: Type identifier for the agent
        """
        self.agent_type = agent_type
        self.system_prompt = system_prompt
        
        # Configure Google Gemini API with global API key
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Initialize Gemini model
        self.model = genai.GenerativeModel(
            model_name=GEMINI_MODEL,
            generation_config={
                "temperature": 0.7,
                "top_p": 0.95,
                "top_k": 40,
                "max_output_tokens": 2048,
            }
        )
        
        # Default temperature (can be overridden per call)
        self.temperature = 0.7
        
    def call_gemini(self, user_message: str, **kwargs) -> str:
        """
        Make an API call to Google Gemini
        
        Args:
            user_message: The user's input message
            **kwargs: Additional parameters for the API call
            
        Returns:
            The model's response text
        """
        try:
            # Combine system prompt with user message
            full_prompt = f"{self.system_prompt}\n\nUser Input: {user_message}"
            
            # Override temperature if provided
            temperature = kwargs.get("temperature", self.temperature)
            
            # Generate response
            response = self.model.generate_content(
                full_prompt,
                generation_config={
                    "temperature": temperature,
                    "top_p": kwargs.get("top_p", 0.95),
                    "top_k": kwargs.get("top_k", 40),
                    "max_output_tokens": kwargs.get("max_output_tokens", 2048),
                }
            )
            
            return response.text
            
        except Exception as e:
            return f"Error calling Gemini API: {str(e)}"
    
    def process(self, input_text: str) -> Dict[str, Any]:
        """
        Process input - to be implemented by subclasses
        
        Args:
            input_text: Input text to process
            
        Returns:
            Dictionary with processing results
        """
        raise NotImplementedError("Subclasses must implement process method")
    
    def get_type(self) -> str:
        """Return the agent type"""
        return self.agent_type
