@echo off
REM Master Launcher - Starts both Backend and Frontend
REM Double-click this file to launch the entire application

title Agentic AI App Launcher
color 0A

echo.
echo ========================================
echo    AGENTIC AI APPLICATION LAUNCHER
echo ========================================
echo.
echo [*] Starting Backend (Python Flask)...
echo [*] Starting Frontend (Node.js React)...
echo.
echo This will open 2 terminal windows:
echo   1. Backend Server (Port 5000)
echo   2. Frontend Server (Port 3000)
echo.
echo Your browser will open automatically once ready.
echo ========================================
echo.

REM Start backend in new window
start "Backend Server - Port 5000" cmd /k "cd /d "%~dp0backend" && start_backend.bat"

REM Wait a moment for backend to initialize
timeout /t 3 /nobreak >nul

REM Start frontend in new window
start "Frontend Server - Port 3000" cmd /k "cd /d "%~dp0frontend" && start_frontend.bat"

REM Wait for servers to start (longer on first run with npm install)
echo [*] Waiting for servers to initialize...
echo [*] This may take 30-60 seconds on first run while installing dependencies...
timeout /t 20 /nobreak >nul

REM Open browser
echo [*] Opening browser...
start http://localhost:3000

echo.
echo Note: If the page doesn't load, wait a bit longer for npm install to complete,
echo then refresh your browser (F5)

echo.
echo ========================================
echo [√] Application launched successfully!
echo.
echo Frontend: http://localhost:3000
echo Backend:  http://localhost:5000
echo.
echo Close the server windows to stop the app.
echo ========================================
echo.
echo Press any key to exit this launcher...
pause >nul
