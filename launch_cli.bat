@echo off
REM SQL Agent CLI Launcher - Project Submission Ready

echo 🛡️ SQL Agent Security ^& Analytics Masterclass 🛡️
echo Launching interactive demonstration...
echo.

REM Get the directory where this batch file is located
cd /d "%~dp0"

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is required but not found!
    echo    Please install Python 3.8+ and try again.
    pause
    exit /b 1
)

REM Check if virtual environment exists
if exist "..\\.venv\\Scripts\\python.exe" (
    set PYTHON_CMD="..\\.venv\\Scripts\\python.exe"
    echo ✅ Using virtual environment Python
) else (
    set PYTHON_CMD=python
    echo ⚠️ Using system Python ^(virtual environment not found^)
)

REM Check if main file exists
if not exist "main.py" (
    echo ❌ main.py not found!
    echo    Please ensure you're in the correct directory.
    pause
    exit /b 1
)

REM Launch the main CLI
echo 🚀 Starting SQL Agent demonstration...
%PYTHON_CMD% main.py
pause
