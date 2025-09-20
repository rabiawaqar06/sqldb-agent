#!/usr/bin/env python3
"""
Test script to verify the environment setup and API key configuration.
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def test_environment():
    """Test if the environment is properly configured."""
    print("🔧 Testing Environment Configuration...")
    print("=" * 50)
    
    # Check if virtual environment is active
    if hasattr(os.sys, 'real_prefix') or (hasattr(os.sys, 'base_prefix') and os.sys.base_prefix != os.sys.prefix):
        print("✅ Virtual environment is active")
    else:
        print("⚠️  Virtual environment might not be active")
    
    # Check for API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if api_key and api_key != 'your-gemini-api-key-here':
        print("✅ Google API key is configured")
        print(f"   Key starts with: {api_key[:10]}...")
    else:
        print("❌ Google API key is not configured")
        print("   Please set GOOGLE_API_KEY in your .env file")
        print("   Get your key from: https://makersuite.google.com/app/apikey")
        return False
    
    # Test basic imports
    try:
        from langchain_google_genai import ChatGoogleGenerativeAI
        print("✅ LangChain Google GenAI import successful")
    except ImportError as e:
        print(f"❌ LangChain Google GenAI import failed: {e}")
        return False
    
    try:
        from langchain_community.utilities import SQLDatabase
        print("✅ LangChain Community imports successful")
    except ImportError as e:
        print(f"❌ LangChain Community imports failed: {e}")
        return False
    
    # Test database file
    import pathlib
    db_path = pathlib.Path("SQLAgent/sql_agent_class.db")
    if db_path.exists():
        print("✅ Database file exists")
        print(f"   Location: {db_path.absolute()}")
    else:
        print("❌ Database file not found")
        print(f"   Expected location: {db_path.absolute()}")
        return False
    
    # Test LLM initialization
    try:
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
        print("✅ LLM initialization successful")
        
        # Test a simple query
        response = llm.invoke("Hello, this is a test. Please respond with 'Test successful!'")
        print("✅ LLM API call successful")
        print(f"   Response: {response.content}")
        
    except Exception as e:
        print(f"❌ LLM test failed: {e}")
        return False
    
    print("\n🎉 All tests passed! Your environment is ready.")
    return True

if __name__ == "__main__":
    test_environment()
