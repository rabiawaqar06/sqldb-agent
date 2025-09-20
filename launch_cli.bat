@echo off
REM SQL Agent CLI Launcher for Windows
REM Activates virtual environment and launches the interactive CLI

echo 🛡️ SQL Agent Security ^& Analytics Masterclass 🛡️
echo Launching interactive CLI...
echo.

REM Check if virtual environment exists
if not exist ".venv" (
    echo ❌ Virtual environment not found!
    echo    Please run: python -m venv .venv
    echo    Then: .venv\Scripts\activate
    echo    And: pip install -r requirements.txt
    pause
    exit /b 1
)

REM Activate virtual environment
call .venv\Scripts\activate.bat

REM Check if Python packages are installed
python -c "import langchain_google_genai" 2>nul
if errorlevel 1 (
    echo ⚠️  Dependencies not installed or virtual environment not activated
    echo    Installing dependencies...
    pip install -r requirements.txt
)

REM Launch CLI
python sql_agent_cli.py
pause
