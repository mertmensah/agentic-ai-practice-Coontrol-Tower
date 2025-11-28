"""
Global Configuration Settings
Contains API keys and application settings
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ========================================
# GOOGLE GEMINI API KEY (GLOBAL VARIABLE)
# ========================================
# SECURITY: Get API key from environment variable
# DO NOT hardcode the API key here!
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "your-api-key-here")

# Application Settings
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
FLASK_ENV = os.getenv("FLASK_ENV", "development")

# CORS Settings
ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "http://localhost:3000").split(",")

# Gemini Model Configuration
GEMINI_MODEL = "models/gemini-2.5-flash"  # Stable, fast, and reliable
GEMINI_TIMEOUT = 30  # seconds

# Database Configuration (if needed in future)
DATABASE_URL = os.getenv("DATABASE_URL", None)
