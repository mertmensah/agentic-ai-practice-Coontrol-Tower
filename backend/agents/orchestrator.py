"""
Multi-Agent Orchestrator
Coordinates multiple AI agents working together
"""
from typing import Dict, Any, List
from .content_moderator_agent import ContentModeratorAgent
from .cat_translator_agent import CatTranslatorAgent

class MultiAgentOrchestrator:
    """
    Orchestrates multiple agents to process text through a pipeline
    
    Pipeline:
    1. Content Moderator checks if text is workplace appropriate
    2. If appropriate, Cat Translator converts to cat language
    """
    
    def __init__(self):
        self.moderator = ContentModeratorAgent()
        self.cat_translator = CatTranslatorAgent()
        
    def process_pipeline(self, input_text: str, skip_moderation: bool = False) -> Dict[str, Any]:
        """
        Process text through the multi-agent pipeline
        
        Args:
            input_text: Text to process
            skip_moderation: If True, skip moderation and translate directly
            
        Returns:
            Dictionary with results from all agents
        """
        results = {
            "input": input_text,
            "pipeline": []
        }
        
        # Step 1: Content Moderation
        if not skip_moderation:
            moderation_result = self.moderator.process(input_text)
            results["pipeline"].append({
                "step": 1,
                "agent": "ContentModeratorAgent",
                "result": moderation_result
            })
            
            # Check if we should proceed (in a real system, parse the JSON response)
            # For now, we'll proceed regardless for demonstration
            results["moderation"] = moderation_result
        
        # Step 2: Cat Translation
        translation_result = self.cat_translator.process(input_text)
        results["pipeline"].append({
            "step": 2 if not skip_moderation else 1,
            "agent": "CatTranslatorAgent",
            "result": translation_result
        })
        
        results["final_output"] = translation_result["cat_translation"]
        results["status"] = "completed"
        
        return results
    
    def process_single_agent(self, input_text: str, agent_type: str) -> Dict[str, Any]:
        """
        Process text with a single agent
        
        Args:
            input_text: Text to process
            agent_type: Either 'moderator' or 'translator'
            
        Returns:
            Result from the specified agent
        """
        if agent_type == "moderator":
            return self.moderator.process(input_text)
        elif agent_type == "translator":
            return self.cat_translator.process(input_text)
        else:
            return {
                "error": f"Unknown agent type: {agent_type}",
                "available_agents": ["moderator", "translator"]
            }
    
    def get_agents_info(self) -> Dict[str, Any]:
        """
        Get information about all available agents
        """
        return {
            "agents": [
                {
                    "name": "ContentModeratorAgent",
                    "type": "moderator",
                    "description": "Checks if text is workplace appropriate"
                },
                {
                    "name": "CatTranslatorAgent",
                    "type": "translator",
                    "description": "Converts text to cat language (meows)"
                }
            ],
            "pipeline_mode": "Sequential processing through both agents",
            "single_mode": "Process with individual agents"
        }
