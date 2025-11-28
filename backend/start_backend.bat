@echo off
REM Backend Launcher Script for Windows
REM This script starts the Flask backend server

echo ========================================
echo   Starting Backend Server (Python/Flask)
echo ========================================
echo.

REM Navigate to backend directory
cd /d "%~dp0"

REM Check if virtual environment exists
if not exist "venv\" (
    echo [!] Virtual environment not found. Creating one...
    py -m venv venv
    echo [√] Virtual environment created.
    echo.
)

REM Activate virtual environment
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies if needed
echo [*] Checking dependencies...
pip install -r requirements.txt --quiet

echo.
echo [√] Backend server starting on http://localhost:5000
echo [!] Press Ctrl+C to stop the server
echo ========================================
echo.

REM Start Flask app
py app.py

pause
