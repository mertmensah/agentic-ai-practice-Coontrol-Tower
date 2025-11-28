"""
List all available Gemini models
"""
import google.generativeai as genai
import sys
import os

# Add parent directory to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.settings import GEMINI_API_KEY

# Configure API
genai.configure(api_key=GEMINI_API_KEY)

print("=" * 60)
print("AVAILABLE GEMINI MODELS")
print("=" * 60)
print()

try:
    # List all available models
    for model in genai.list_models():
        # Check if model supports generateContent
        if 'generateContent' in model.supported_generation_methods:
            print(f"✓ {model.name}")
            print(f"  Display Name: {model.display_name}")
            print(f"  Description: {model.description}")
            print(f"  Supported Methods: {model.supported_generation_methods}")
            print()
except Exception as e:
    print(f"Error: {e}")
    print()
    print("Please check your API key in backend/config/settings.py")
