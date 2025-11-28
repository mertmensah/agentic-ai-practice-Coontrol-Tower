# Agentic AI Web Application

A full-stack web application with Python backend (agentic AI using Google Gemini) and Node.js frontend.

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
