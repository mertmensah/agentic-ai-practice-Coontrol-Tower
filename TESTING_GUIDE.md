# Multi-Agent AI System Testing Guide

## System Overview

This system uses **2 specialized AI agents** powered by **Google Gemini API**:

### Agent 1: Content Moderator
- **Purpose**: Checks if text is workplace appropriate
- **AI Model**: Google Gemini Pro
- **System Prompt**: Configured to act as a professional content moderator
- **Parameters**: Temperature 0.3 (more consistent/strict)

### Agent 2: Cat Translator  
- **Purpose**: Converts text to cat language (meows)
- **AI Model**: Google Gemini Pro
- **System Prompt**: Configured to translate to creative cat expressions
- **Parameters**: Temperature 0.9 (more creative/playful)

## Important: API Key Configuration

The Gemini API key is set as a **global variable** in the configuration file:

**Location**: `backend/config/settings.py`

```python
# Global Variable (loaded from environment)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "your-api-key-here")
```

✅ **Configuration Required:** Set your API key in `.env` file:

### Setting Up Environment Variables
Create `backend/.env` file:
```bash
GEMINI_API_KEY=your-actual-api-key-here
```

⚠️ **Get your API key from:** https://makersuite.google.com/app/apikey

## API Endpoints

### 1. Full Pipeline (Both Agents)
```bash
POST /api/agents/pipeline
Body: {
    "text": "Your text here",
    "skip_moderation": false  # optional
}
```

### 2. Content Moderator Only
```bash
POST /api/agents/moderate
Body: {
    "text": "Your text here"
}
```

### 3. Cat Translator Only
```bash
POST /api/agents/translate
Body: {
    "text": "Your text here"
}
```

### 4. Get Agents Info
```bash
GET /api/agents/info
```

## Testing with cURL (PowerShell)

### Test the Pipeline
```powershell
$body = @{text="Hello, how are you today?"} | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:5000/api/agents/pipeline -Method Post -Body $body -ContentType "application/json"
```

### Test Content Moderator
```powershell
$body = @{text="This is a professional message"} | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:5000/api/agents/moderate -Method Post -Body $body -ContentType "application/json"
```

### Test Cat Translator
```powershell
$body = @{text="I love you!"} | ConvertTo-Json
Invoke-RestMethod -Uri http://localhost:5000/api/agents/translate -Method Post -Body $body -ContentType "application/json"
```

## How It Works

### Architecture
```
User Input
    ↓
[Content Moderator Agent] → Uses Google Gemini API with moderation prompt
    ↓
[Cat Translator Agent] → Uses Google Gemini API with translation prompt
    ↓
Final Output
```

### Key Points
1. **Same Model, Different Prompts**: Both agents use Google Gemini Pro but with different system prompts
2. **No Fine-Tuning Needed**: Agents are defined through prompts, not custom models
3. **Sequential Processing**: Agents run one after another in a pipeline
4. **Independent Usage**: Can call each agent individually or together
5. **Global API Key**: Configured once in `config/settings.py`, used by all agents

## Cost Considerations

- Each agent call = 1 Google Gemini API request
- Pipeline mode = 2 API requests (one per agent)
- Google Gemini pricing is competitive with other AI models
- Set `max_output_tokens=2048` to limit response length/cost

## Example Responses

### Content Moderator Response:
```json
{
    "appropriate": true,
    "reason": "Text is professional and appropriate",
    "severity": "none",
    "original_text": "Hello team, great work!"
}
```

### Cat Translator Response:
```json
{
    "original_text": "I'm so happy!",
    "cat_translation": "MEOW MEOW MEOW! 😻 Purrrr!",
    "agent": "CatTranslatorAgent"
}
```

### Full Pipeline Response:
```json
{
    "input": "Great job everyone!",
    "pipeline": [
        {
            "step": 1,
            "agent": "ContentModeratorAgent",
            "result": {...}
        },
        {
            "step": 2,
            "agent": "CatTranslatorAgent",
            "result": {...}
        }
    ],
    "final_output": "Mrow mrow mrrp! 😸"
}
```
