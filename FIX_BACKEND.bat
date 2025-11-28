@echo off
REM Quick Fix Script - Reinstall Backend Dependencies

echo ========================================
echo   Reinstalling Backend Dependencies
echo ========================================
echo.

cd /d "%~dp0backend"

echo [*] Activating virtual environment...
call venv\Scripts\activate.bat

echo [*] Installing Google Gemini package...
pip install google-generativeai==0.3.2

echo.
echo [√] Done! Now close all server windows and run START_APP.bat again.
echo.
pause
