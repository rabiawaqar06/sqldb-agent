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

#!/bin/bash
# SQL Agent CLI Launcher - Project Submission Ready

echo "🛡️ SQL Agent Security & Analytics Masterclass 🛡️"
echo "Launching interactive demonstration..."
echo

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not found!"
    echo "   Please install Python 3.8+ and try again."
    exit 1
fi

# Check if virtual environment exists
VENV_PATH="../.venv/bin/python"
if [ -f "$VENV_PATH" ]; then
    PYTHON_CMD="$VENV_PATH"
    echo "✅ Using virtual environment Python"
else
    PYTHON_CMD="python3"
    echo "⚠️  Using system Python (virtual environment not found)"
fi

# Check if main file exists
if [ ! -f "main.py" ]; then
    echo "❌ main.py not found!"
    echo "   Please ensure you're in the correct directory."
    exit 1
fi

# Launch the main CLI
echo "🚀 Starting SQL Agent demonstration..."
"$PYTHON_CMD" main.py
