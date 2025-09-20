#!/usr/bin/env python3
"""
Quick test of the basic LLM functionality with Gemini
"""

from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

def test_basic_llm():
    """Test basic LLM functionality"""
    print("🤖 Testing basic LLM with Gemini...")
    
    # Initialize the LLM
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
    
    # Test a simple query
    response = llm.invoke("What is 2 + 2? Please answer briefly.")
    print(f"LLM Response: {response.content}")
    
    print("✅ Basic LLM test completed successfully!")

if __name__ == "__main__":
    test_basic_llm()
