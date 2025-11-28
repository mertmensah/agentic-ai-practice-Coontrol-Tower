"""
Image Generation Agent
Generates cat images using Pollinations.ai (Free, no API key needed)
"""
from typing import Dict, Any
import google.generativeai as genai
import requests
import io
import base64
from PIL import Image
import sys
import os
import urllib.parse

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import GEMINI_API_KEY

class ImageGenerationAgent:
    """
    Agent that generates cat images using Pollinations.ai
    Free, fast, no API key required!
    """
    
    def __init__(self):
        self.agent_type = "ImageGenerationAgent"
        genai.configure(api_key=GEMINI_API_KEY)
        
        # Using Pollinations.ai - completely free, no API key
        self.api_url = "https://image.pollinations.ai/prompt/"
        
    def generate_image(self, prompt: str) -> Dict[str, Any]:
        """
        Generate cat image from text prompt using Pollinations.ai
        
        Args:
            prompt: Text description of desired cat image
            
        Returns:
            Dictionary with image generation results
        """
        try:
            # Enhance the prompt to focus on cats
            enhanced_prompt = self.enhance_prompt(prompt)
            
            print(f"Generating image with prompt: {enhanced_prompt}")
            print(f"Using Pollinations.ai API")
            
            # URL encode the prompt
            encoded_prompt = urllib.parse.quote(enhanced_prompt)
            
            # Build the URL (Pollinations.ai generates on the fly)
            image_url = f"{self.api_url}{encoded_prompt}?width=1024&height=1024&nologo=true"
            
            print(f"Fetching image from: {image_url}")
            
            # Download the image
            response = requests.get(image_url, timeout=30)
            response.raise_for_status()
            
            print("Image downloaded successfully, converting to base64...")
            
            # Convert to PIL Image
            image = Image.open(io.BytesIO(response.content))
            
            # Convert to base64 for frontend
            buffered = io.BytesIO()
            image.save(buffered, format="PNG")
            img_str = base64.b64encode(buffered.getvalue()).decode()
            
            # Return data URL
            image_data_url = f"data:image/png;base64,{img_str}"
            
            print("Image conversion complete!")
            
            return {
                "agent": self.agent_type,
                "prompt": prompt,
                "enhanced_prompt": enhanced_prompt,
                "image_url": image_data_url,
                "message": "Image generated successfully!",
                "status": "success"
            }
            
        except requests.Timeout:
            error_msg = "Image generation timed out. Please try again."
            print(f"ERROR: {error_msg}")
            return {
                "agent": self.agent_type,
                "prompt": prompt,
                "image_url": None,
                "message": error_msg,
                "status": "error"
            }
        except requests.RequestException as e:
            error_msg = f"Network error: {str(e)}"
            print(f"ERROR: {error_msg}")
            return {
                "agent": self.agent_type,
                "prompt": prompt,
                "image_url": None,
                "message": error_msg,
                "status": "error"
            }
        except Exception as e:
            error_msg = str(e)
            print(f"ERROR generating image: {error_msg}")
            
            return {
                "agent": self.agent_type,
                "prompt": prompt,
                "image_url": None,
                "message": f"Failed to generate image: {error_msg}",
                "status": "error"
            }
    
    def enhance_prompt(self, user_prompt: str) -> str:
        """
        Enhance user prompt with cat-specific details for better image generation
        """
        try:
            model = genai.GenerativeModel("models/gemini-2.5-flash")
            
            enhancement_prompt = f"""
            Enhance this cat image generation prompt to be more detailed and specific for Stable Diffusion.
            
            User prompt: "{user_prompt}"
            
            Add details about:
            - Specific breed characteristics if mentioned
            - Fur texture and patterns
            - Eye color and expression
            - Pose and environment
            - Lighting and artistic style
            
            Keep it under 75 words. Focus on visual details. Return ONLY the enhanced prompt, nothing else.
            """
            
            response = model.generate_content(enhancement_prompt)
            enhanced = response.text.strip()
            
            # Ensure "cat" is in the prompt for better results
            if "cat" not in enhanced.lower():
                enhanced = f"cat, {enhanced}"
            
            # Add quality modifiers for Stable Diffusion
            enhanced = f"{enhanced}, highly detailed, professional photography, 4k"
            
            return enhanced
            
        except Exception as e:
            print(f"Error enhancing prompt: {str(e)}")
            # Fallback to basic enhancement
            return f"beautiful cat, {user_prompt}, highly detailed, professional photography, 4k"
    
    def get_type(self) -> str:
        return self.agent_type

