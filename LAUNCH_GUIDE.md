# 🚀 Quick Start Guide

## Launch the Application

### ✨ Easy Way (Double-Click to Launch)

Simply **double-click** the file in the root directory:

```
START_APP.bat
```

This will:
1. ✅ Start the Python backend server (Port 5000)
2. ✅ Start the Node.js frontend server (Port 3000)
3. ✅ Automatically open your browser to the app

---

## Manual Launch (Alternative)

If you prefer to start servers separately:

### Backend (Python)
```bash
cd backend
start_backend.bat
```

### Frontend (Node.js)
```bash
cd frontend
start_frontend.bat
```

Then open: http://localhost:3000

---

## 🎨 UI Design

The app features an **Uber-inspired design** with:
- ⬛ Sleek black background
- 🟢 Green accent colors (#05C167)
- 🎯 Minimalist, clean interface
- ✨ Smooth animations
- 💬 Modern chat bubbles
- 📱 Responsive design

---

## ⚙️ Before First Run

### ✅ API Key Already Configured!

The Google Gemini API key is loaded from environment variables in:

**`backend/config/settings.py`**
```python
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "your-api-key-here")
```

**Configuration Required:** Create `backend/.env` file with your API key:
```bash
GEMINI_API_KEY=your-actual-api-key-here
```

⚠️ **Get your API key from:** https://makersuite.google.com/app/apikey

### 2. Install Dependencies (First Time Only)

The launcher scripts will handle this automatically, or run manually:

**Backend:**
```bash
cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

**Frontend:**
```bash
cd frontend
npm install
```

---

## 🧪 Test the Multi-Agent System

Once running, try these messages:

1. **"Hello, how are you today?"** - Gets moderated then translated to cat language
2. **"I'm so excited!"** - See enthusiastic cat meows
3. **"Thank you for helping me"** - Polite cat purrs

The system runs your text through:
1. 🛡️ Content Moderator (checks appropriateness)
2. 🐱 Cat Translator (converts to meows)

---

## 🔧 Troubleshooting

### Port Already in Use
- Backend (5000): Stop any other Flask/Python servers
- Frontend (3000): Stop any other React/Node servers

### Dependencies Not Installing
- Ensure Python 3.8+ is installed
- Ensure Node.js 16+ is installed
- Run PowerShell as Administrator if needed

### API Key Issues
- The Gemini API key is pre-configured in `backend/config/settings.py`
- If you need a new key, get one from: https://makersuite.google.com/app/apikey
- Update the `GEMINI_API_KEY` variable in `backend/config/settings.py`

---

## 📂 Project Structure

```
├── START_APP.bat           ← Double-click this to launch!
├── backend/
│   ├── start_backend.bat   ← Backend launcher
│   ├── app.py              ← Flask server
│   └── agents/             ← AI agent code
└── frontend/
    ├── start_frontend.bat  ← Frontend launcher
    └── src/                ← React UI code
```

---

## 🎯 Next Steps

- Customize the UI colors in `frontend/src/styles/App.css`
- Add more agents in `backend/agents/`
- Modify agent prompts in the agent files
- Deploy to production using Docker

Enjoy your Agentic AI application! 🚀
