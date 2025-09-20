#!/bin/bash
# SQL Agent CLI Launcher
# Activates virtual environment and launches the interactive CLI

echo "🛡️ SQL Agent Security & Analytics Masterclass 🛡️"
echo "Launching interactive CLI..."
echo

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "❌ Virtual environment not found!"
    echo "   Please run: python -m venv .venv"
    echo "   Then: source .venv/bin/activate"
    echo "   And: pip install -r requirements.txt"
    exit 1
fi

# Activate virtual environment
source .venv/bin/activate

# Check if Python packages are installed
if ! python -c "import langchain_google_genai" 2>/dev/null; then
    echo "⚠️  Dependencies not installed or virtual environment not activated"
    echo "   Installing dependencies..."
    pip install -r requirements.txt
fi

# Launch CLI
python sql_agent_cli.py
