#!/usr/bin/env python3
"""
SQL Agent Security & Analytics Masterclass
Main Interactive CLI - Project Submission Ready

A comprehensive educational project demonstrating SQL agent security,
from basic implementations to production-ready secure agents.

Features:
- Multiple security levels (Educational → Secure → Production)
- Interactive chat with Google Gemini AI
- Business intelligence and analytics
- Real-time SQL query execution with safety checks
- Comprehensive educational scripts

Author: SQL Agent Security Course
Technology: LangChain + Google Gemini AI + SQLite
"""

import os
import sys
from sql_agent_cli import SQLAgentCLI

def print_welcome():
    """Display welcome message and project information"""
    print("🛡️" + "="*80 + "🛡️")
    print("   SQL AGENT SECURITY & ANALYTICS MASTERCLASS")
    print("             Final Project Submission")
    print("         Powered by Google Gemini AI & LangChain")
    print("🛡️" + "="*80 + "🛡️")
    print()
    print("📚 This project demonstrates:")
    print("   • Progressive SQL agent security implementation")
    print("   • Multiple interaction modes for different use cases")
    print("   • Business intelligence and analytics capabilities")
    print("   • Production-ready security guardrails")
    print("   • Educational scripts showcasing security concepts")
    print()
    print("🎯 Project Components:")
    print("   • Interactive CLI with 5 specialized chat modes")
    print("   • Educational scripts (basic → secure → production)")
    print("   • Real e-commerce database with 6 tables")
    print("   • Comprehensive security features and validation")
    print()

def check_environment():
    """Check if environment is properly configured"""
    print("🔧 Checking Environment...")
    print("-" * 40)
    
    # Check API key
    api_key = os.getenv('GOOGLE_API_KEY')
    if not api_key:
        print("❌ GOOGLE_API_KEY not found in environment!")
        print("   Please set your API key:")
        print("   export GOOGLE_API_KEY='your-api-key-here'")
        print("   Or create a .env file with GOOGLE_API_KEY=your-api-key")
        return False
    else:
        print(f"✅ Google API Key configured (starts with: {api_key[:10]}...)")
    
    # Check database
    db_path = "SQLAgent/sql_agent_class.db"
    if os.path.exists(db_path):
        print(f"✅ Database found: {db_path}")
    else:
        print(f"❌ Database not found: {db_path}")
        return False
    
    # Check imports
    try:
        import langchain
        from langchain_google_genai import ChatGoogleGenerativeAI
        print("✅ LangChain and Google GenAI imports successful")
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("   Please install requirements: pip install -r requirements.txt")
        return False
    
    print("✅ Environment check passed!")
    print()
    return True

def main():
    """Main entry point for the SQL Agent CLI"""
    print_welcome()
    
    if not check_environment():
        print("⚠️  Please fix environment issues before continuing.")
        sys.exit(1)
    
    print("🚀 Launching Interactive CLI...")
    print("   All features are ready for demonstration!")
    print()
    
    # Launch the main CLI
    try:
        cli = SQLAgentCLI()
        cli.run()
    except KeyboardInterrupt:
        print("\n\n👋 Thank you for exploring SQL Agent Security!")
        print("   Project demonstration complete. 🎊")
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
        print("   Please check your environment configuration.")

if __name__ == "__main__":
    main()
