@echo off
REM SQL Agent CLI Launcher - Project Submission Ready
REM Direct launch without requiring virtual environment

echo 🛡️ SQL Agent Security ^& Analytics Masterclass 🛡️
echo Launching interactive demonstration...
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is required but not found!
    echo    Please install Python 3.8+ and try again.
    pause
    exit /b 1
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
python main.py
pause
