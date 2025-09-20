#!/usr/bin/env python3
"""
Demo script to showcase SQL Agent CLI capabilities
This script demonstrates the CLI features without requiring user interaction
"""

import sys
import os
from pathlib import Path

# Add current directory to path
sys.path.append(str(Path(__file__).parent))

# Import the CLI class
from sql_agent_cli import SQLAgentCLI

def demo_cli_features():
    """Demonstrate CLI features without user interaction"""
    
    print("🎮 SQL Agent CLI Demo")
    print("=" * 50)
    
    cli = SQLAgentCLI()
    
    # Test header display
    print("\n1. Testing header display:")
    cli.print_header()
    
    # Test menu display
    print("\n2. Testing main menu:")
    cli.print_menu()
    
    # Test environment check capabilities
    print("\n3. Testing environment check capabilities:")
    print("   - Project root:", cli.project_root)
    print("   - SQL Agent dir:", cli.sql_agent_dir)
    print("   - Scripts dir:", cli.scripts_dir)
    print("   - Scripts exist:", cli.scripts_dir.exists())
    
    # Test API key checking
    print("\n4. Testing API key check:")
    api_key = os.getenv('GOOGLE_API_KEY')
    if api_key:
        if api_key == 'your-gemini-api-key-here':
            print("   ⚠️  Default API key found - please update your .env file")
        else:
            print("   ✅ Google API key is configured")
    else:
        print("   ❌ No Google API key found")
    
    # Test database verification
    print("\n5. Testing database verification:")
    db_path = cli.sql_agent_dir / "sql_agent_class.db"
    if db_path.exists():
        print(f"   ✅ Database file exists at {db_path}")
        print(f"   📊 Database size: {db_path.stat().st_size} bytes")
    else:
        print("   ❌ Database file not found")
    
    # Test script discovery
    print("\n6. Testing script discovery:")
    scripts = [
        "00_simple_llm.py",
        "01_simple_agent.py", 
        "02_risky_delete_demo.py",
        "03_guardrailed_agent.py",
        "04_complex_queries.py",
        "reset_db.py"
    ]
    
    for script in scripts:
        script_path = cli.scripts_dir / script
        status = "✅" if script_path.exists() else "❌"
        print(f"   {status} {script}")
    
    print("\n7. Testing file structure verification:")
    required_files = [
        cli.project_root / ".env",
        cli.project_root / "requirements.txt",
        cli.project_root / "test_setup.py",
        cli.project_root / "quick_test.py",
        cli.sql_agent_dir / "README.md",
        cli.sql_agent_dir / "sql_agent_seed.sql"
    ]
    
    for file_path in required_files:
        status = "✅" if file_path.exists() else "❌"
        print(f"   {status} {file_path.name}")
    
    print("\n🎉 CLI Demo Complete!")
    print("=" * 50)
    print("✨ The interactive CLI is ready to use!")
    print("   Run: ./launch_cli.sh (Linux/Mac) or launch_cli.bat (Windows)")
    print("   Or directly: python sql_agent_cli.py")

if __name__ == "__main__":
    demo_cli_features()
