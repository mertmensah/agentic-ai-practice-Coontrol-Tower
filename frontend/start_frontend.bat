@echo off
REM Frontend Launcher Script for Windows
REM This script starts the Vite development server

echo ========================================
echo   Starting Frontend Server (Node.js/React)
echo ========================================
echo.

REM Navigate to frontend directory
cd /d "%~dp0"

REM Check if node_modules exists
if not exist "node_modules\" (
    echo [!] Node modules not found. Installing dependencies...
    call npm install
    echo [√] Dependencies installed.
    echo.
)

echo [√] Frontend server starting on http://localhost:3000
echo [!] Press Ctrl+C to stop the server
echo ========================================
echo.

REM Start Vite dev server
call npm run dev

pause
