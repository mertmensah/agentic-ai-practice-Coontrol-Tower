# 🐱 Cat Management Platform - Agentic AI Demo

> A comprehensive AI-powered platform for cat communication, image generation, and breed identification. Built with Google Gemini AI, React, and Flask.

**🔗 [Live Demo](https://YOUR_USERNAME.github.io/YOUR_REPO_NAME/)** | **📖 [Deployment Guide](DEPLOYMENT_GUIDE.md)** | **🆕 [New Features](NEW_FEATURES.md)**

![Platform Screenshot](https://via.placeholder.com/1200x600/000000/05C167?text=Cat+Management+Platform)

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

## 📁 Project Structure

```
Agentic-AI-Learning-Demo/
├── backend/
│   ├── agents/
│   │   ├── orchestrator.py              # Multi-agent coordinator
│   │   ├── content_moderator_agent.py   # Content filtering
│   │   ├── cat_translator_agent.py      # Language translation
│   │   ├── breed_match_agent.py         # Breed identification
│   │   ├── image_generation_agent.py    # Image generation
│   │   └── video_generation_agent.py    # Video generation (placeholder)
│   ├── config/
│   │   └── settings.py                  # API keys & configuration
│   ├── app.py                          # Flask API server
│   └── requirements.txt                # Python dependencies
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
│   │       └── platform.css            # Uber-style theme
│   ├── package.json
│   └── vite.config.js
│
├── START_APP.bat                       # Windows one-click launcher
├── DEPLOYMENT_GUIDE.md                 # Full deployment instructions
├── NEW_FEATURES.md                     # Feature documentation
└── README.md                           # This file
```

## 🌐 Deploy to Production

Deploy your app online for FREE using:
- **Backend**: Render.com (free tier)
- **Frontend**: GitHub Pages (unlimited free hosting)

**See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for step-by-step instructions.**

Quick summary:
1. Push code to GitHub
2. Deploy backend to Render
3. Deploy frontend to GitHub Pages
4. Update environment variables
5. Done! 🎉

## 🔑 Configuration

### API Keys

Edit `backend/config/settings.py`:

```python
# Google Gemini API Key
GEMINI_API_KEY = "your-api-key-here"

# Model Configuration
GEMINI_MODEL = "models/gemini-2.5-flash"
```

Get your free Gemini API key: https://makersuite.google.com/app/apikey

### Environment Variables

**Development** (`frontend/.env`):
```
VITE_API_URL=http://localhost:5000
```

**Production** (`frontend/.env.production`):
```
VITE_API_URL=https://your-backend.onrender.com
```

## 🎨 Features Showcase

### Voice Recognition
- Real-time speech-to-text in the browser
- No external APIs needed
- Works in Chrome, Edge, Safari
- Visual feedback with pulsing red button

### AI Image Generation
- Powered by Stable Diffusion
- Automatic prompt enhancement
- Breed identification
- Content moderation
- Base64 embedded images (no storage needed)

### Multi-Agent Architecture
- Orchestrator pattern for agent coordination
- Content moderation on all inputs
- Specialized agents for different tasks
- Extensible design for new features

## 🔧 Troubleshooting

**Backend won't start:**
- Check Python version: `python --version` (need 3.11+)
- Install dependencies: `pip install -r requirements.txt`
- Verify Gemini API key in `settings.py`

**Frontend won't start:**
- Check Node version: `node --version` (need 18+)
- Clear node_modules: `rm -rf node_modules && npm install`
- Check port 3000 isn't already in use

**Voice input not working:**
- Use Chrome, Edge, or Safari (not Firefox)
- Allow microphone permissions
- Requires HTTPS in production

**Image generation fails:**
- Check internet connection
- First generation may take 30+ seconds
- Verify backend server is running

## 📝 License

MIT License - feel free to use this project however you want!

## 🤝 Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests
- Improve documentation

## 👨‍💻 Author

Built as an Agentic AI learning demonstration.

## 🙏 Acknowledgments

- **Google Gemini** - AI language model
- **Pollinations.ai** - Free image generation
- **Uber** - Design inspiration
- **React** & **Flask** - Framework foundations

---

**Made with 💚 and lots of ☕ for cat lovers everywhere!** 🐱✨
