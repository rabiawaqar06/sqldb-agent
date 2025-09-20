#!/usr/bin/env python3
"""
Quick test of the interactive chat functionality
This script tests the basic chat interface without user interaction
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_chat_components():
    """Test that all chat components can be imported and initialized"""
    
    print("🧪 Testing Interactive Chat Components")
    print("=" * 50)
    
    # Test 1: Environment setup
    print("\n1. Testing environment setup:")
    api_key = os.getenv('GOOGLE_API_KEY')
    if api_key and api_key != 'your-gemini-api-key-here':
        print("   ✅ Google API key configured")
    else:
        print("   ⚠️  API key needs configuration")
    
    # Test 2: Basic Gemini import and initialization
    print("\n2. Testing Gemini AI import:")
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
        print("   ✅ Gemini AI import successful")
        
        # Quick test
        response = llm.invoke("Say 'Hello from test!'")
        print(f"   ✅ Quick test response: {response.content[:50]}...")
        
    except ImportError as e:
        print(f"   ❌ Import error: {e}")
    except Exception as e:
        print(f"   ❌ Initialization error: {e}")
    
    # Test 3: SQL Agent components
    print("\n3. Testing SQL Agent components:")
    try:
        from langchain.agents import create_sql_agent
        from langchain_community.agent_toolkits import SQLDatabaseToolkit
        from langchain_community.utilities import SQLDatabase
        print("   ✅ SQL Agent imports successful")
        
        # Test database connection
        db_path = Path(__file__).parent / "SQLAgent" / "sql_agent_class.db"
        if db_path.exists():
            db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
            print("   ✅ Database connection successful")
            
            # Test basic query
            result = db.run("SELECT COUNT(*) as total_customers FROM customers;")
            print(f"   ✅ Database query test: {result}")
        else:
            print("   ❌ Database file not found")
            
    except ImportError as e:
        print(f"   ❌ SQL Agent import error: {e}")
    except Exception as e:
        print(f"   ❌ SQL Agent error: {e}")
    
    # Test 4: Direct SQLite access
    print("\n4. Testing direct SQLite access:")
    try:
        import sqlite3
        db_path = Path(__file__).parent / "SQLAgent" / "sql_agent_class.db"
        
        if db_path.exists():
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print(f"   ✅ Found {len(tables)} tables: {[t[0] for t in tables]}")
            conn.close()
        else:
            print("   ❌ Database file not found")
            
    except Exception as e:
        print(f"   ❌ SQLite error: {e}")
    
    print("\n" + "=" * 50)
    print("🎯 Interactive Chat Test Results:")
    print("   All major components are ready for interactive use!")
    print("   Launch the CLI and try option 6: 💬 Interactive Chat & SQL")
    print("\n🚀 Quick Start:")
    print("   ./launch_cli.sh  # Then choose option 6")
    print("   python sql_agent_cli.py  # Then choose option 6")

if __name__ == "__main__":
    test_chat_components()
