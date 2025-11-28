# 🐱 Cat Management Platform - Agentic AI Demo

> A comprehensive AI-powered platform for cat communication, image generation, and breed identification. Built with Google Gemini AI, React, and Flask.

**🔗 [Live Demo](https://mertmensah.github.io/agentic-ai-practice-Coontrol-Tower/)** | **📖 [Deployment Guide](DEPLOYMENT_GUIDE.md)** | **🆕 [New Features](NEW_FEATURES.md)**

---

## ✨ Features

### 🎛️ Coontrol Tower (Dashboard)
- Real-time system monitoring with live clock
- Module overview with statistics
- System health indicators
- Beautiful Uber-inspired dark theme

### 🗣️ Text/Speech to Cat Translator
- **Voice Input** - Web Speech API for hands-free operation
- **AI Translation** - Converts human language to cat language using Gemini AI
- **Content Moderation** - Ensures workplace-appropriate content
- **Real-time Processing** - Instant translations

### 🎨 Dream Cat Generator
- **AI Image Generation** - Creates cat images from text descriptions
- **Prompt Enhancement** - Gemini AI automatically optimizes your prompts
- **Breed Matching** - Identifies cat breeds from descriptions
- **Free & Instant** - Powered by Pollinations.ai (no API key needed)

### 🎬 Cat Video Generator
- Upload cat images
- Generate animated videos/GIFs
- Multiple format support (MP4, GIF)
- *(Coming soon - UI ready)*

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         THE USER                             │
│                  (Your Browser/Device)                       │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ HTTPS Request
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              FRONTEND (GitHub Pages)                         │
│   https://mertmensah.github.io/agentic-ai-practice...       │
│                                                              │
│   React App (Static Files)                                  │
│   - HTML, CSS, JavaScript                                   │
│   - Runs entirely in user's browser                         │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ API Calls (Axios)
                       ▼
┌─────────────────────────────────────────────────────────────┐
│              BACKEND (Render.com)                            │
│        https://cat-platform-backend.onrender.com             │
│                                                              │
│   Flask Server (Python)                                     │
│   - Handles API requests                                    │
│   - Coordinates AI agents                                   │
│   - Returns JSON responses                                  │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       │ API Calls
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                   EXTERNAL AI SERVICES                       │
│                                                              │
│  ┌──────────────────┐  ┌─────────────────┐  ┌────────────┐ │
│  │ Google Gemini AI │  │ Pollinations.ai │  │ Web Speech │ │
│  │ (Text/Language)  │  │ (Image Gen)     │  │ (Browser)  │ │
│  └──────────────────┘  └─────────────────┘  └────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

---

## 🚀 Quick Start

### One-Click Local Setup

**Windows:**
```bash
START_APP.bat
```

This automatically:
1. Starts the Python backend server
2. Starts the React frontend dev server
3. Opens your browser to http://localhost:3000

### Manual Setup

**Prerequisites:**
- Python 3.11+
- Node.js 18+
- Git

**Backend:**
```bash
cd backend
pip install -r requirements.txt
python app.py
```

**Frontend:**
```bash
cd frontend
npm install
npm run dev
```

---

## 🎮 Usage

### Voice Translation
1. Navigate to "Text/Speech to Cat"
2. Click the 🎤 Voice button
3. Allow microphone permissions
4. Speak your message
5. Get instant cat language translation!

### Image Generation
1. Navigate to "Dream Cat Generator"
2. Describe your dream cat (e.g., "A fluffy orange tabby with green eyes")
3. Click "Generate Dream Cat"
4. Wait 10-20 seconds
5. Admire your AI-generated cat! 🎨

---

## 🛠️ Tech Stack

### Frontend
- **React 18.2** - Modern UI library
- **Vite 5.0** - Lightning-fast build tool
- **Axios 1.6** - HTTP client
- **Web Speech API** - Browser-based voice input

### Backend
- **Flask 3.0** - Python web framework
- **Google Gemini 2.5 Flash** - AI language model
- **Pollinations.ai** - Free image generation
- **Pillow 10.2** - Image processing

### APIs & Services
- **Google Gemini API** - Text generation, moderation, translation
- **Pollinations.ai** - Stable Diffusion image generation
- **Web Speech API** - Speech-to-text recognition

---

## 📁 Project Structure

```
agentic-ai-practice-Coontrol-Tower/
├── backend/
│   ├── agents/
│   │   ├── orchestrator.py              # Multi-agent coordinator
│   │   ├── content_moderator_agent.py   # Content filtering
│   │   ├── cat_translator_agent.py      # Language translation
│   │   ├── breed_match_agent.py         # Breed identification
│   │   ├── image_generation_agent.py    # Image generation
│   │   ├── video_generation_agent.py    # Video generation (placeholder)
│   │   └── simple_agent.py              # Base agent class
│   ├── config/
│   │   └── settings.py                  # Configuration & API keys
│   ├── app.py                          # Flask API server
│   ├── requirements.txt                # Python dependencies
│   └── runtime.txt                     # Python version (3.11.9)
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── CoontrolTower.jsx       # Dashboard
│   │   │   ├── TextToCat.jsx           # Voice/text translator
│   │   │   ├── DreamCatGenerator.jsx   # Image generator
│   │   │   ├── CatVideoGenerator.jsx   # Video generator
│   │   │   └── Sidebar.jsx             # Navigation
│   │   ├── services/
│   │   │   └── api.js                  # API service layer
│   │   └── styles/
│   │       └── platform.css            # Uber-style theme (800+ lines)
│   ├── package.json
│   ├── vite.config.js
│   └── .env.production                 # Production API URL
│
├── START_APP.bat                       # Windows one-click launcher
├── Procfile                            # Render deployment config
├── DEPLOYMENT_GUIDE.md                 # Full deployment instructions
├── NEW_FEATURES.md                     # Feature documentation
└── README.md                           # This file
```

---

## 🔧 Multi-Agent Architecture

The backend uses a **multi-agent pattern** where specialized AI agents handle different tasks:

```
backend/agents/
│
├── orchestrator.py          # 🎭 Coordinator
│   └── Routes requests to correct agents
│       Manages the pipeline flow
│
├── content_moderator_agent.py   # 🛡️ Safety Check
│   └── Uses Gemini to check if content is appropriate
│       Temperature: 0.3 (strict, consistent)
│
├── cat_translator_agent.py      # 😺 Language Expert
│   └── Converts human language → cat language
│       Temperature: 0.9 (creative, varied)
│
├── breed_match_agent.py         # 🐾 Breed Identifier
│   └── Identifies cat breeds from descriptions
│       Temperature: 0.4 (accurate, factual)
│
├── image_generation_agent.py   # 🎨 Artist
│   └── Generates cat images via Pollinations.ai
│       Uses Gemini to enhance prompts first
│
└── video_generation_agent.py   # 🎬 (Placeholder)
    └── Ready for future video AI integration
```

**Agent Pipeline Example:**
```
User Request → Orchestrator → Content Moderator → Cat Translator → Response
                                     ↓
                            (Rejects if inappropriate)
```

---

## 🔄 Data Flow Example

### Generating a Cat Image:

1. **User Input:** Types "fluffy orange cat" and clicks "Generate"

2. **Frontend (React):** 
   ```javascript
   const response = await generateDreamCat(formData)
   ```

3. **API Call:** 
   ```
   POST https://cat-platform-backend.onrender.com/api/dream-cat/generate
   ```

4. **Backend Processing:**
   - Content Moderator checks prompt ✅
   - Breed Matcher analyzes description 🐾
   - Gemini enhances prompt 🧠
   - Pollinations.ai generates image 🎨
   - Image converted to base64 📦

5. **Response:** JSON with image data URL, breed info, status

6. **Display:** React renders image in browser

---

## 🌐 Live Deployment

### **Frontend (Your App):**
```
https://mertmensah.github.io/agentic-ai-practice-Coontrol-Tower/
```

### **Backend API:**
```
https://cat-platform-backend.onrender.com
```

### **Hosting:**
- **Frontend:** GitHub Pages (free, unlimited)
- **Backend:** Render.com (free tier)

---

## 🔑 Configuration

### API Keys

You'll need a Google Gemini API key. Get one free at: https://makersuite.google.com/app/apikey

Edit `backend/config/settings.py`:

```python
# Google Gemini API Key
GEMINI_API_KEY = "your-api-key-here"

# Model Configuration
GEMINI_MODEL = "models/gemini-2.5-flash"
```

**For Render Deployment:**
Add `GEMINI_API_KEY` as an environment variable in your Render dashboard.

### Environment Variables

**Development** (`frontend/.env`):
```
VITE_API_URL=http://localhost:5000
```

**Production** (`frontend/.env.production`):
```
VITE_API_URL=https://your-backend.onrender.com
```

---

## 🚀 Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for complete step-by-step instructions.

**Quick Summary:**
1. Push code to GitHub
2. Deploy backend to Render.com
3. Deploy frontend to GitHub Pages with `npm run deploy`
4. Configure environment variables
5. Done! 🎉

---

## 🎨 Design System

**Theme:** Uber-inspired dark mode

```css
Colors:
- Black: #000000 (background)
- Green: #05C167 (primary actions)
- Dark Gray: #1a1a1a (cards)
- White: #FFFFFF (text)

Layout:
- Sidebar: 280px (expanded) / 70px (collapsed)
- Max width: 1400px (content)
- Responsive breakpoints at 1024px
```

---

## 🔧 Development Workflow

### Local Development:
```bash
# Make changes to code
# Test with START_APP.bat
```

### Deploy Changes:
```bash
# Commit and push
git add .
git commit -m "Your changes"
git push

# Backend auto-deploys to Render (2-3 min)

# Deploy frontend (if changed):
cd frontend
npm run deploy
```

---

## ⚡ Performance

### Frontend (GitHub Pages):
- Load time: < 2 seconds
- Globally distributed CDN
- HTTPS included

### Backend (Render Free Tier):
- Cold start: 30-60 seconds (after 15 min inactivity)
- Warm response: < 1 second
- Auto-sleeps after 15 minutes idle

### AI Processing:
- Gemini text: 1-3 seconds
- Image generation: 10-20 seconds
- Voice recognition: Real-time (browser)

---

## 🔧 Troubleshooting

**Backend won't start locally:**
- Check Python version: `python --version` (need 3.11+)
- Install dependencies: `pip install -r requirements.txt`
- Verify Gemini API key in `backend/config/settings.py`

**Frontend won't start:**
- Check Node version: `node --version` (need 18+)
- Clear and reinstall: `rm -rf node_modules && npm install`

**Voice input not working:**
- Use Chrome, Edge, or Safari (not Firefox)
- Allow microphone permissions
- Requires HTTPS in production (GitHub Pages provides this)

**Image generation slow/fails:**
- First request takes 30-60 seconds (Render cold start)
- Check internet connection
- Verify backend is running

---

## 📊 Project Stats

- **Total Lines of Code:** ~9,300+
- **Technologies Used:** 15+
- **Deployment Platforms:** 3
- **AI Services Integrated:** 3
- **Languages:** Python, JavaScript, HTML, CSS
- **Frameworks:** Flask, React, Vite

---

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 📝 License

MIT License - feel free to use this project however you want!

---

## 🙏 Acknowledgments

- **Google Gemini** - AI language model
- **Pollinations.ai** - Free image generation
- **Uber** - Design inspiration
- **React** & **Flask** - Framework foundations

---

**Made with 💚 and lots of ☕ for cat lovers everywhere!** 🐱✨

## Project Structure

```
Agentic AI Learning Demo/
├── backend/                 # Python backend for AI agents
│   ├── agents/             # AI agent implementations
│   ├── api/                # API endpoints
│   ├── config/             # Configuration files (API keys)
│   ├── utils/              # Utility functions
│   ├── requirements.txt    # Python dependencies
│   ├── app.py             # Main Flask application
│   └── .env               # Environment variables
│
├── frontend/               # Node.js frontend
│   ├── public/            # Static files
│   ├── src/               # Source code
│   │   ├── components/    # React components
│   │   ├── services/      # API service calls
│   │   ├── styles/        # CSS/styling files
│   │   └── App.js         # Main application file
│   ├── package.json       # Node.js dependencies
│   └── .env               # Frontend environment variables
│
├── shared/                 # Shared resources
│   └── types/             # Shared type definitions
│
└── START_APP.bat          # One-click launcher
```

## Technology Stack

### Backend (Python)
- **Framework**: Flask
- **AI/ML**: Google Gemini API (gemini-pro)
- **API Key**: Configured globally in `config/settings.py`
- **Dependencies**: Listed in `requirements.txt`

### Frontend (Node.js)
- **Framework**: React.js
- **Build Tool**: Vite
- **API Client**: Axios
- **Styling**: Uber-inspired custom CSS

## Getting Started

### Quick Start (Recommended)
Simply double-click `START_APP.bat` in the root directory!

### Backend Setup
```bash
cd backend
python -m venv venv
venv\Scripts\activate  # On Windows
pip install -r requirements.txt
python app.py
```

### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## API Communication
- Backend runs on: `http://localhost:5000`
- Frontend runs on: `http://localhost:3000`
- Frontend calls backend API endpoints for AI agent operations

## Key Features
- 🤖 Multi-agent AI system using Google Gemini
- 🛡️ Content moderation for workplace appropriateness
- 🐱 Creative cat language translation
- 💬 Interactive web interface with Uber-style design
- 🔄 Sequential agent pipeline processing
