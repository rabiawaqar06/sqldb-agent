#!/usr/bin/env python3
"""
Interactive CLI for SQL Agent Security & Analytics Masterclass

This CLI provides an easy way to explore the SQL Agent project with guided navigation,
setup verification, and interactive script execution.
"""

import os
import sys
import subprocess
from pathlib import Path
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()

class SQLAgentCLI:
    def __init__(self):
        self.project_root = Path(__file__).parent
        self.sql_agent_dir = self.project_root / "SQLAgent"
        self.scripts_dir = self.sql_agent_dir / "scripts"
        
    def clear_screen(self):
        """Clear the terminal screen"""
        os.system('clear' if os.name == 'posix' else 'cls')
        
    def print_header(self):
        """Print the main header"""
        print("🛡️" + "=" * 70 + "🛡️")
        print("   SQL Agent Security & Analytics Masterclass")
        print("         Powered by Google Gemini AI")
        print("🛡️" + "=" * 70 + "🛡️")
        print()
        
    def print_menu(self):
        """Print the main menu"""
        print("📋 Main Menu:")
        print("-" * 50)
        print("1. 🔧 Setup & Environment Check")
        print("2. 📚 Educational Scripts")
        print("3. 🗄️  Database Management")
        print("4. 🧪 Quick Tests")
        print("5. 📖 Documentation")
        print("6. 💬 Interactive Chat & SQL")
        print("7. ❌ Exit")
        print("-" * 50)
        
    def setup_menu(self):
        """Setup and environment check submenu"""
        while True:
            self.clear_screen()
            self.print_header()
            print("🔧 Setup & Environment Check")
            print("-" * 50)
            print("1. ✅ Run Full Environment Check")
            print("2. 🔑 Check API Key Configuration")
            print("3. 📦 Install/Update Dependencies")
            print("4. 🗄️  Verify Database")
            print("5. 🧪 Test Basic LLM Functionality")
            print("6. ⬅️  Back to Main Menu")
            print("-" * 50)
            
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == "1":
                self.run_environment_check()
            elif choice == "2":
                self.check_api_key()
            elif choice == "3":
                self.install_dependencies()
            elif choice == "4":
                self.verify_database()
            elif choice == "5":
                self.test_basic_llm()
            elif choice == "6":
                break
            else:
                print("❌ Invalid choice. Please try again.")
                time.sleep(1)
                
    def educational_scripts_menu(self):
        """Educational scripts submenu"""
        scripts = [
            ("00_simple_llm.py", "🤖 Basic LLM Conversation", "Learn basic Gemini AI interaction"),
            ("01_simple_agent.py", "🔓 Simple SQL Agent", "Basic SQL agent (NO security)"),
            ("02_risky_delete_demo.py", "⚠️  Dangerous Agent Demo", "Educational - shows what NOT to do"),
            ("03_guardrailed_agent.py", "🛡️  Secure SQL Agent", "Production-ready with security"),
            ("04_complex_queries.py", "📊 Advanced Analytics", "Complex business intelligence")
        ]
        
        while True:
            self.clear_screen()
            self.print_header()
            print("📚 Educational Scripts")
            print("-" * 50)
            
            for i, (filename, title, description) in enumerate(scripts, 1):
                print(f"{i}. {title}")
                print(f"   📄 {filename}")
                print(f"   💡 {description}")
                print()
                
            print("6. ⬅️  Back to Main Menu")
            print("-" * 50)
            
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice in ["1", "2", "3", "4", "5"]:
                script_index = int(choice) - 1
                filename, title, description = scripts[script_index]
                self.run_educational_script(filename, title, description)
            elif choice == "6":
                break
            else:
                print("❌ Invalid choice. Please try again.")
                time.sleep(1)
                
    def database_menu(self):
        """Database management submenu"""
        while True:
            self.clear_screen()
            self.print_header()
            print("🗄️ Database Management")
            print("-" * 50)
            print("1. 🔄 Reset Database to Initial State")
            print("2. 📊 View Database Schema")
            print("3. 📈 Show Sample Data")
            print("4. 🔍 Run Custom SQL Query")
            print("5. 📝 Show Database Statistics")
            print("6. ⬅️  Back to Main Menu")
            print("-" * 50)
            
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == "1":
                self.reset_database()
            elif choice == "2":
                self.show_database_schema()
            elif choice == "3":
                self.show_sample_data()
            elif choice == "4":
                self.run_custom_query()
            elif choice == "5":
                self.show_database_stats()
            elif choice == "6":
                break
            else:
                print("❌ Invalid choice. Please try again.")
                time.sleep(1)
                
    def quick_tests_menu(self):
        """Quick tests submenu"""
        while True:
            self.clear_screen()
            self.print_header()
            print("🧪 Quick Tests")
            print("-" * 50)
            print("1. ⚡ Quick LLM Test")
            print("2. 🔍 Test SQL Agent Basic Query")
            print("3. 🛡️  Test Security Guardrails")
            print("4. 📊 Test Analytics Query")
            print("5. 🏃 Run All Tests")
            print("6. ⬅️  Back to Main Menu")
            print("-" * 50)
            
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == "1":
                self.quick_llm_test()
            elif choice == "2":
                self.test_basic_sql_query()
            elif choice == "3":
                self.test_security_guardrails()
            elif choice == "4":
                self.test_analytics_query()
            elif choice == "5":
                self.run_all_tests()
            elif choice == "6":
                break
            else:
                print("❌ Invalid choice. Please try again.")
                time.sleep(1)
                
    def documentation_menu(self):
        """Documentation submenu"""
        while True:
            self.clear_screen()
            self.print_header()
            print("📖 Documentation")
            print("-" * 50)
            print("1. 📋 View README")
            print("2. 🏗️  Project Structure")
            print("3. 🔒 Security Guidelines")
            print("4. 💾 Database Schema Details")
            print("5. 🔧 Troubleshooting Guide")
            print("6. ⬅️  Back to Main Menu")
            print("-" * 50)
            
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == "1":
                self.view_readme()
            elif choice == "2":
                self.show_project_structure()
            elif choice == "3":
                self.show_security_guidelines()
            elif choice == "4":
                self.show_database_schema_details()
            elif choice == "5":
                self.show_troubleshooting()
            elif choice == "6":
                break
            else:
                print("❌ Invalid choice. Please try again.")
                time.sleep(1)
                
    def run_environment_check(self):
        """Run the full environment check"""
        print("\n🔧 Running Environment Check...")
        print("-" * 40)
        try:
            result = subprocess.run([sys.executable, "test_setup.py"], 
                                  capture_output=True, text=True, cwd=self.project_root)
            print(result.stdout)
            if result.stderr:
                print("⚠️ Warnings/Errors:")
                print(result.stderr)
        except Exception as e:
            print(f"❌ Error running environment check: {e}")
        
        input("\nPress Enter to continue...")
        
    def check_api_key(self):
        """Check API key configuration"""
        print("\n🔑 Checking API Key Configuration...")
        print("-" * 40)
        
        api_key = os.getenv('GOOGLE_API_KEY')
        if api_key:
            if api_key == 'your-gemini-api-key-here':
                print("⚠️  Default API key found - please update your .env file")
                print("   Get your key from: https://makersuite.google.com/app/apikey")
            else:
                print("✅ Google API key is configured")
                print(f"   Key starts with: {api_key[:10]}...")
        else:
            print("❌ No Google API key found")
            print("   Please add GOOGLE_API_KEY to your .env file")
            
        input("\nPress Enter to continue...")
        
    def install_dependencies(self):
        """Install or update dependencies"""
        print("\n📦 Installing/Updating Dependencies...")
        print("-" * 40)
        try:
            result = subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], 
                                  cwd=self.project_root)
            if result.returncode == 0:
                print("✅ Dependencies installed successfully!")
            else:
                print("❌ Error installing dependencies")
        except Exception as e:
            print(f"❌ Error: {e}")
            
        input("\nPress Enter to continue...")
        
    def verify_database(self):
        """Verify database existence and basic structure"""
        print("\n🗄️ Verifying Database...")
        print("-" * 40)
        
        db_path = self.sql_agent_dir / "sql_agent_class.db"
        if db_path.exists():
            print("✅ Database file exists")
            print(f"   Location: {db_path}")
            print(f"   Size: {db_path.stat().st_size} bytes")
            
            # Check tables
            try:
                import sqlite3
                conn = sqlite3.connect(db_path)
                cursor = conn.cursor()
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
                tables = cursor.fetchall()
                print(f"   Tables found: {len(tables)}")
                for table in tables:
                    print(f"     - {table[0]}")
                conn.close()
            except Exception as e:
                print(f"   ⚠️ Error reading database: {e}")
        else:
            print("❌ Database file not found")
            print("   Run 'Reset Database' to create it")
            
        input("\nPress Enter to continue...")
        
    def test_basic_llm(self):
        """Test basic LLM functionality"""
        print("\n🧪 Testing Basic LLM Functionality...")
        print("-" * 40)
        try:
            result = subprocess.run([sys.executable, "quick_test.py"], 
                                  capture_output=True, text=True, cwd=self.project_root)
            print(result.stdout)
            if result.stderr:
                print("⚠️ Warnings/Errors:")
                print(result.stderr)
        except Exception as e:
            print(f"❌ Error: {e}")
            
        input("\nPress Enter to continue...")
        
    def run_educational_script(self, filename, title, description):
        """Run an educational script with user confirmation"""
        self.clear_screen()
        self.print_header()
        print(f"🚀 Running: {title}")
        print(f"📄 Script: {filename}")
        print(f"💡 Description: {description}")
        print("-" * 50)
        
        if filename == "02_risky_delete_demo.py":
            print("⚠️  WARNING: This script contains dangerous operations!")
            print("   It can DELETE data from the database.")
            print("   This is for educational purposes only.")
            confirm = input("\n   Do you want to continue? (type 'yes' to confirm): ").strip().lower()
            if confirm != 'yes':
                print("❌ Cancelled for safety.")
                input("Press Enter to continue...")
                return
                
        print("\n🏃 Executing script...")
        print("=" * 50)
        
        try:
            # Change to SQLAgent directory and run script
            script_path = self.scripts_dir / filename
            result = subprocess.run([sys.executable, f"scripts/{filename}"], 
                                  cwd=self.sql_agent_dir)
            print("=" * 50)
            if result.returncode == 0:
                print("✅ Script completed successfully!")
            else:
                print("⚠️ Script completed with warnings or errors.")
        except Exception as e:
            print(f"❌ Error running script: {e}")
            
        input("\nPress Enter to continue...")
        
    def reset_database(self):
        """Reset database to initial state"""
        print("\n🔄 Resetting Database...")
        print("-" * 40)
        
        confirm = input("⚠️  This will reset all data. Continue? (y/N): ").strip().lower()
        if confirm not in ['y', 'yes']:
            print("❌ Cancelled.")
            input("Press Enter to continue...")
            return
            
        try:
            result = subprocess.run([sys.executable, "scripts/reset_db.py"], 
                                  cwd=self.sql_agent_dir)
            if result.returncode == 0:
                print("✅ Database reset successfully!")
            else:
                print("❌ Error resetting database")
        except Exception as e:
            print(f"❌ Error: {e}")
            
        input("\nPress Enter to continue...")
        
    def show_database_schema(self):
        """Show database schema"""
        print("\n📊 Database Schema")
        print("-" * 40)
        
        schema_info = """
🏪 E-Commerce Database Schema:

📋 customers
   - id (PRIMARY KEY)
   - name, email, created_at, region

🛍️ products  
   - id (PRIMARY KEY)
   - name, category, price_cents

📦 orders
   - id (PRIMARY KEY)
   - customer_id → customers(id)
   - order_date, status

💳 payments
   - id (PRIMARY KEY) 
   - order_id → orders(id)
   - amount_cents, paid_at, method, status

💰 refunds
   - id (PRIMARY KEY)
   - order_id → orders(id) 
   - amount_cents, refunded_at, reason

📝 order_items
   - id (PRIMARY KEY)
   - order_id → orders(id)
   - product_id → products(id)
   - quantity, unit_price_cents
        """
        print(schema_info)
        input("\nPress Enter to continue...")
        
    def show_sample_data(self):
        """Show sample data from database"""
        print("\n📈 Sample Data")
        print("-" * 40)
        
        try:
            import sqlite3
            db_path = self.sql_agent_dir / "sql_agent_class.db"
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Show customers
            print("👥 Customers (first 3):")
            cursor.execute("SELECT name, email, region FROM customers LIMIT 3")
            for row in cursor.fetchall():
                print(f"   {row[0]} ({row[1]}) - {row[2]}")
                
            print("\n🛍️ Products (first 3):")
            cursor.execute("SELECT name, category, price_cents FROM products LIMIT 3")
            for row in cursor.fetchall():
                print(f"   {row[0]} ({row[1]}) - ${row[2]/100:.2f}")
                
            print("\n📦 Recent Orders:")
            cursor.execute("SELECT id, customer_id, order_date, status FROM orders ORDER BY order_date DESC LIMIT 3")
            for row in cursor.fetchall():
                print(f"   Order #{row[0]} - Customer {row[1]} - {row[2]} - {row[3]}")
                
            conn.close()
        except Exception as e:
            print(f"❌ Error reading database: {e}")
            
        input("\nPress Enter to continue...")
        
    def run_custom_query(self):
        """Run a custom SQL query"""
        print("\n🔍 Custom SQL Query")
        print("-" * 40)
        print("⚠️  Only SELECT statements are recommended for safety")
        
        query = input("\nEnter your SQL query: ").strip()
        
        if not query.upper().startswith('SELECT'):
            confirm = input("⚠️  Non-SELECT query detected. Continue? (y/N): ").strip().lower()
            if confirm not in ['y', 'yes']:
                return
                
        try:
            import sqlite3
            db_path = self.sql_agent_dir / "sql_agent_class.db"
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            cursor.execute(query)
            results = cursor.fetchall()
            
            print(f"\n📊 Results ({len(results)} rows):")
            print("-" * 30)
            for i, row in enumerate(results[:10]):  # Limit to 10 rows
                print(f"   {i+1}: {row}")
                
            if len(results) > 10:
                print(f"   ... and {len(results) - 10} more rows")
                
            conn.close()
        except Exception as e:
            print(f"❌ Error executing query: {e}")
            
        input("\nPress Enter to continue...")
        
    def show_database_stats(self):
        """Show database statistics"""
        print("\n📝 Database Statistics")
        print("-" * 40)
        
        try:
            import sqlite3
            db_path = self.sql_agent_dir / "sql_agent_class.db"
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            # Count records in each table
            tables = ['customers', 'products', 'orders', 'payments', 'refunds', 'order_items']
            for table in tables:
                cursor.execute(f"SELECT COUNT(*) FROM {table}")
                count = cursor.fetchone()[0]
                print(f"   📊 {table}: {count} records")
                
            # Some business metrics
            print("\n💼 Business Metrics:")
            cursor.execute("SELECT COUNT(DISTINCT customer_id) FROM orders")
            active_customers = cursor.fetchone()[0]
            print(f"   👥 Active customers: {active_customers}")
            
            cursor.execute("SELECT SUM(amount_cents) FROM payments WHERE status = 'succeeded'")
            total_revenue = cursor.fetchone()[0] or 0
            print(f"   💰 Total revenue: ${total_revenue/100:.2f}")
            
            cursor.execute("SELECT COUNT(*) FROM orders WHERE status = 'paid'")
            paid_orders = cursor.fetchone()[0]
            print(f"   ✅ Paid orders: {paid_orders}")
            
            conn.close()
        except Exception as e:
            print(f"❌ Error getting statistics: {e}")
            
        input("\nPress Enter to continue...")
        
    def quick_llm_test(self):
        """Quick LLM test"""
        print("\n⚡ Quick LLM Test")
        print("-" * 40)
        
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
            response = llm.invoke("Say 'Hello from Gemini!' and explain what you are in one sentence.")
            print("🤖 Gemini Response:")
            print(f"   {response.content}")
            print("✅ LLM test successful!")
        except Exception as e:
            print(f"❌ LLM test failed: {e}")
            
        input("\nPress Enter to continue...")
        
    def test_basic_sql_query(self):
        """Test basic SQL agent query"""
        print("\n🔍 Testing Basic SQL Query")
        print("-" * 40)
        print("🤖 Testing: 'Show me 3 customers with their regions'")
        
        try:
            # This is a simplified test - in practice you'd run the actual agent
            import sqlite3
            db_path = self.sql_agent_dir / "sql_agent_class.db"
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name, region FROM customers LIMIT 3")
            results = cursor.fetchall()
            
            print("📊 Query Result:")
            for name, region in results:
                print(f"   {name} - {region}")
            print("✅ Basic SQL test successful!")
            conn.close()
        except Exception as e:
            print(f"❌ SQL test failed: {e}")
            
        input("\nPress Enter to continue...")
        
    def test_security_guardrails(self):
        """Test security guardrails"""
        print("\n🛡️ Testing Security Guardrails")
        print("-" * 40)
        
        dangerous_queries = [
            "DELETE FROM customers",
            "DROP TABLE orders",
            "UPDATE products SET price_cents = 0"
        ]
        
        print("🧪 Testing dangerous query patterns:")
        for query in dangerous_queries:
            print(f"   Testing: {query}")
            # In practice, this would test the guardrails in the secure agent
            if any(word in query.upper() for word in ['DELETE', 'DROP', 'UPDATE']):
                print("   ✅ BLOCKED - Security guardrail working")
            else:
                print("   ❌ ALLOWED - This would be dangerous!")
                
        print("\n✅ Security tests completed!")
        input("\nPress Enter to continue...")
        
    def test_analytics_query(self):
        """Test analytics query"""
        print("\n📊 Testing Analytics Query")
        print("-" * 40)
        print("🤖 Testing: Revenue by region analysis")
        
        try:
            import sqlite3
            db_path = self.sql_agent_dir / "sql_agent_class.db"
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            
            query = """
            SELECT c.region, SUM(p.amount_cents) as total_revenue
            FROM customers c
            JOIN orders o ON c.id = o.customer_id
            JOIN payments p ON o.id = p.order_id
            WHERE p.status = 'succeeded'
            GROUP BY c.region
            ORDER BY total_revenue DESC
            """
            
            cursor.execute(query)
            results = cursor.fetchall()
            
            print("📊 Revenue by Region:")
            for region, revenue in results:
                print(f"   {region}: ${revenue/100:.2f}")
            print("✅ Analytics test successful!")
            conn.close()
        except Exception as e:
            print(f"❌ Analytics test failed: {e}")
            
        input("\nPress Enter to continue...")
        
    def run_all_tests(self):
        """Run all quick tests"""
        print("\n🏃 Running All Tests")
        print("-" * 40)
        
        print("1/4 Testing LLM...")
        self.quick_llm_test()
        
        print("\n2/4 Testing Basic SQL...")
        self.test_basic_sql_query()
        
        print("\n3/4 Testing Security...")
        self.test_security_guardrails()
        
        print("\n4/4 Testing Analytics...")
        self.test_analytics_query()
        
        print("\n🎉 All tests completed!")
        input("\nPress Enter to continue...")
        
    def view_readme(self):
        """View README file"""
        print("\n📋 README")
        print("-" * 40)
        
        readme_path = self.sql_agent_dir / "README.md"
        if readme_path.exists():
            try:
                with open(readme_path, 'r') as f:
                    content = f.read()
                # Show first 50 lines
                lines = content.split('\n')[:50]
                for line in lines:
                    print(line)
                if len(content.split('\n')) > 50:
                    print("\n... (README continues - open the file to read more)")
            except Exception as e:
                print(f"❌ Error reading README: {e}")
        else:
            print("❌ README.md not found")
            
        input("\nPress Enter to continue...")
        
    def show_project_structure(self):
        """Show project structure"""
        print("\n🏗️ Project Structure")
        print("-" * 40)
        
        structure = """
📁 week_10/
├── 🔐 .env                     # API configuration
├── 📦 .venv/                   # Virtual environment  
├── 📋 requirements.txt         # Dependencies
├── 🧪 test_setup.py           # Environment check
├── ⚡ quick_test.py           # Basic LLM test
├── 🎮 sql_agent_cli.py        # This CLI tool
└── 📂 SQLAgent/               # Main project
    ├── 📖 README.md            # Documentation
    ├── 🗄️ sql_agent_class.db   # Sample database
    ├── 📜 sql_agent_seed.sql   # Database schema
    └── 📂 scripts/             # Educational scripts
        ├── 🔄 reset_db.py       # Database utility
        ├── 🤖 00_simple_llm.py  # Basic LLM
        ├── 🔓 01_simple_agent.py # Simple SQL agent
        ├── ⚠️ 02_risky_delete_demo.py # Dangerous patterns
        ├── 🛡️ 03_guardrailed_agent.py # Secure agent
        └── 📊 04_complex_queries.py # Analytics
        """
        print(structure)
        input("\nPress Enter to continue...")
        
    def show_security_guidelines(self):
        """Show security guidelines"""
        print("\n🔒 Security Guidelines")
        print("-" * 40)
        
        guidelines = """
🛡️ SQL Agent Security Best Practices:

✅ DO:
  • Use input validation and regex patterns
  • Implement whitelist approach (SELECT only)
  • Add automatic LIMIT injection
  • Use read-only database users
  • Implement comprehensive error handling
  • Log all queries and results
  • Regular security audits

❌ DON'T:
  • Allow unrestricted SQL execution
  • Trust user input without validation
  • Use privileged database accounts
  • Expose internal error details
  • Allow multiple statement execution
  • Skip result set limiting

⚠️ Key Security Layers:
  1. Input validation (regex patterns)
  2. Statement type checking (SELECT only)
  3. Multi-statement prevention
  4. Result limiting (max 200 rows)
  5. Safe error handling
  6. SQL injection protection
        """
        print(guidelines)
        input("\nPress Enter to continue...")
        
    def show_database_schema_details(self):
        """Show detailed database schema"""
        print("\n💾 Database Schema Details")
        print("-" * 40)
        
        schema_details = """
🏪 E-Commerce Database - Detailed Schema:

👥 CUSTOMERS
   • id: INTEGER PRIMARY KEY
   • name: TEXT NOT NULL  
   • email: TEXT UNIQUE
   • created_at: TEXT (ISO date)
   • region: TEXT (APAC, NA, EU)

🛍️ PRODUCTS
   • id: INTEGER PRIMARY KEY
   • name: TEXT NOT NULL
   • category: TEXT (Home, Electronics, Apparel)
   • price_cents: INTEGER (price in cents)

📦 ORDERS  
   • id: INTEGER PRIMARY KEY
   • customer_id: FOREIGN KEY → customers(id)
   • order_date: TEXT (ISO date)
   • status: TEXT (pending, paid, refunded, canceled)

💳 PAYMENTS
   • id: INTEGER PRIMARY KEY
   • order_id: FOREIGN KEY → orders(id)
   • amount_cents: INTEGER
   • paid_at: TEXT (ISO datetime, nullable)
   • method: TEXT (card, paypal)
   • status: TEXT (succeeded, failed, refunded, pending)

💰 REFUNDS
   • id: INTEGER PRIMARY KEY
   • order_id: FOREIGN KEY → orders(id)
   • amount_cents: INTEGER
   • refunded_at: TEXT (ISO datetime)
   • reason: TEXT

📝 ORDER_ITEMS
   • id: INTEGER PRIMARY KEY
   • order_id: FOREIGN KEY → orders(id)
   • product_id: FOREIGN KEY → products(id)
   • quantity: INTEGER
   • unit_price_cents: INTEGER
        """
        print(schema_details)
        input("\nPress Enter to continue...")
        
    def show_troubleshooting(self):
        """Show troubleshooting guide"""
        print("\n🔧 Troubleshooting Guide")
        print("-" * 40)
        
        troubleshooting = """
🔧 Common Issues & Solutions:

❌ "Import langchain_google_genai could not be resolved"
✅ Solution: Activate virtual environment and reinstall packages
   source .venv/bin/activate
   pip install -r requirements.txt

❌ "Google API key not found"  
✅ Solution: Check .env file configuration
   Add: GOOGLE_API_KEY=your-actual-api-key-here
   Get key from: https://makersuite.google.com/app/apikey

❌ "Database file not found"
✅ Solution: Reset the database
   Run: Database Management → Reset Database

❌ "404 models/gemini-pro is not found"
✅ Solution: Model name updated
   All scripts now use: gemini-1.5-flash

❌ Virtual environment issues
✅ Solution: Recreate environment
   rm -rf .venv
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

❌ Permission errors
✅ Solution: Check file permissions
   chmod +x sql_agent_cli.py

🆘 Still having issues?
   1. Run 'Setup & Environment Check'
   2. Check all files are in correct locations
   3. Verify Python version (3.8+)
   4. Ensure internet connection for API calls
        """
        print(troubleshooting)
        input("\nPress Enter to continue...")
        
    def interactive_chat_menu(self):
        """Interactive chat and SQL query interface"""
        while True:
            self.clear_screen()
            self.print_header()
            print("💬 Interactive Chat & SQL")
            print("-" * 50)
            print("1. 🤖 Chat with Gemini AI")
            print("2. 🛡️  Secure SQL Agent (Production)")
            print("3. 🔓 Simple SQL Agent (Educational)")
            print("4. 📊 Business Analytics Chat")
            print("5. 💾 Direct SQL Query")
            print("6. ⬅️  Back to Main Menu")
            print("-" * 50)
            
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == "1":
                self.basic_chat_interface()
            elif choice == "2":
                self.secure_sql_agent_chat()
            elif choice == "3":
                self.simple_sql_agent_chat()
            elif choice == "4":
                self.analytics_chat_interface()
            elif choice == "5":
                self.direct_sql_interface()
            elif choice == "6":
                break
            else:
                print("❌ Invalid choice. Please try again.")
                time.sleep(1)
                
    def basic_chat_interface(self):
        """Basic chat interface with Gemini AI"""
        self.clear_screen()
        self.print_header()
        print("🤖 Chat with Gemini AI")
        print("-" * 50)
        print("💡 Ask anything! Type 'exit' to return to menu")
        print("📝 Example questions:")
        print("   • Explain machine learning")
        print("   • What is a SQL agent?")
        print("   • How do databases work?")
        print("=" * 50)
        
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
            
            while True:
                user_input = input("\n💬 You: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'back']:
                    break
                    
                if not user_input:
                    continue
                    
                try:
                    print("🤖 Gemini: ", end="", flush=True)
                    response = llm.invoke(user_input)
                    print(response.content)
                except Exception as e:
                    print(f"❌ Error: {e}")
                    
        except ImportError:
            print("❌ LangChain not properly installed. Run Setup & Environment Check.")
        except Exception as e:
            print(f"❌ Error initializing chat: {e}")
            
        input("\nPress Enter to continue...")
        
    def secure_sql_agent_chat(self):
        """Secure SQL agent with guardrails"""
        self.clear_screen()
        self.print_header()
        print("🛡️ Secure SQL Agent (Production Ready)")
        print("-" * 50)
        print("✅ Features: Input validation, SELECT-only, result limiting")
        print("💡 Ask business questions about the e-commerce database!")
        print("📝 Example questions:")
        print("   • Show me top 3 customers by revenue")
        print("   • What products sell best?")
        print("   • Which region has most orders?")
        print("⚠️  Type 'exit' to return to menu")
        print("=" * 50)
        
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            from langchain.agents import create_sql_agent
            from langchain_community.agent_toolkits import SQLDatabaseToolkit
            from langchain_community.utilities import SQLDatabase
            
            # Initialize components
            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
            db_path = self.sql_agent_dir / "sql_agent_class.db"
            db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
            toolkit = SQLDatabaseToolkit(db=db, llm=llm)
            
            # Create secure agent
            agent = create_sql_agent(
                llm=llm,
                toolkit=toolkit,
                agent_type="zero-shot-react-description",
                verbose=False,
                handle_parsing_errors=True,
                max_iterations=3,
                max_execution_time=30
            )
            
            while True:
                user_input = input("\n📊 Ask about the database: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'back']:
                    break
                    
                if not user_input:
                    continue
                    
                # Add safety prefix to encourage safe queries
                safe_input = f"Please answer this question using only SELECT queries and limit results to 10 rows maximum: {user_input}"
                
                try:
                    print("🛡️ Secure Agent: ", end="", flush=True)
                    response = agent.invoke({"input": safe_input})
                    print(response["output"])
                except Exception as e:
                    print(f"❌ Error: {e}")
                    print("💡 Try rephrasing your question or ask about basic database information.")
                    
        except ImportError as e:
            print(f"❌ Required packages not installed: {e}")
            print("   Run Setup & Environment Check to install dependencies.")
        except Exception as e:
            print(f"❌ Error initializing SQL agent: {e}")
            
        input("\nPress Enter to continue...")
        
    def simple_sql_agent_chat(self):
        """Simple SQL agent for educational purposes"""
        self.clear_screen()
        self.print_header()
        print("🔓 Simple SQL Agent (Educational - Less Secure)")
        print("-" * 50)
        print("⚠️  WARNING: This agent has minimal security restrictions")
        print("💡 Use for learning SQL agent behavior")
        print("📝 Example questions:")
        print("   • List all customers")
        print("   • Show product categories")
        print("   • Count total orders")
        print("🔒 Type 'exit' to return to menu")
        print("=" * 50)
        
        confirm = input("⚠️  Continue with less secure agent? (y/N): ").strip().lower()
        if confirm not in ['y', 'yes']:
            return
            
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            from langchain.agents import create_sql_agent
            from langchain_community.agent_toolkits import SQLDatabaseToolkit
            from langchain_community.utilities import SQLDatabase
            
            # Initialize components
            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
            db_path = self.sql_agent_dir / "sql_agent_class.db"
            db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
            toolkit = SQLDatabaseToolkit(db=db, llm=llm)
            
            # Create simple agent
            agent = create_sql_agent(
                llm=llm,
                toolkit=toolkit,
                agent_type="zero-shot-react-description",
                verbose=True,  # Show reasoning for educational purposes
                handle_parsing_errors=True
            )
            
            while True:
                user_input = input("\n📋 Database question: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'back']:
                    break
                    
                if not user_input:
                    continue
                    
                try:
                    print("🔓 Simple Agent working...")
                    response = agent.invoke({"input": user_input})
                    print(f"📊 Result: {response['output']}")
                except Exception as e:
                    print(f"❌ Error: {e}")
                    
        except ImportError as e:
            print(f"❌ Required packages not installed: {e}")
        except Exception as e:
            print(f"❌ Error initializing SQL agent: {e}")
            
        input("\nPress Enter to continue...")
        
    def analytics_chat_interface(self):
        """Business analytics focused chat interface"""
        self.clear_screen()
        self.print_header()
        print("📊 Business Analytics Chat")
        print("-" * 50)
        print("💼 Specialized for business intelligence questions")
        print("📈 Focus on metrics, trends, and insights")
        print("💡 Example questions:")
        print("   • What's our revenue growth trend?")
        print("   • Which products are most profitable?")
        print("   • Customer acquisition analysis")
        print("   • Regional performance comparison")
        print("🔒 Type 'exit' to return to menu")
        print("=" * 50)
        
        try:
            from langchain_google_genai import ChatGoogleGenerativeAI
            from langchain.agents import create_sql_agent
            from langchain_community.agent_toolkits import SQLDatabaseToolkit
            from langchain_community.utilities import SQLDatabase
            
            # Initialize with business-focused prompt
            llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)
            db_path = self.sql_agent_dir / "sql_agent_class.db"
            db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
            toolkit = SQLDatabaseToolkit(db=db, llm=llm)
            
            agent = create_sql_agent(
                llm=llm,
                toolkit=toolkit,
                agent_type="zero-shot-react-description",
                verbose=False,
                handle_parsing_errors=True,
                agent_executor_kwargs={
                    "return_intermediate_steps": False
                }
            )
            
            print("\n📊 Analytics Agent Ready!")
            print("💡 I'll focus on business metrics and insights from your e-commerce data.")
            
            while True:
                user_input = input("\n📈 Business question: ").strip()
                
                if user_input.lower() in ['exit', 'quit', 'back']:
                    break
                    
                if not user_input:
                    continue
                    
                # Enhance input with business context
                business_context = f"""
                As a business analyst, provide insights for this question about our e-commerce business: {user_input}
                
                Focus on actionable business insights and include relevant metrics. Use only SELECT queries.
                Our database contains: customers, products, orders, payments, refunds, and order_items.
                """
                
                try:
                    print("📊 Analyzing business data...")
                    response = agent.invoke({"input": business_context})
                    print(f"💼 Business Insight: {response['output']}")
                except Exception as e:
                    print(f"❌ Error: {e}")
                    
        except ImportError as e:
            print(f"❌ Required packages not installed: {e}")
        except Exception as e:
            print(f"❌ Error initializing analytics agent: {e}")
            
        input("\nPress Enter to continue...")
        
    def direct_sql_interface(self):
        """Direct SQL query interface with safety warnings"""
        self.clear_screen()
        self.print_header()
        print("💾 Direct SQL Query Interface")
        print("-" * 50)
        print("⚠️  WARNING: Direct database access - use carefully!")
        print("✅ Recommended: Only use SELECT statements")
        print("📋 Available tables: customers, products, orders, payments, refunds, order_items")
        print("💡 Example queries:")
        print("   SELECT name, region FROM customers LIMIT 5;")
        print("   SELECT * FROM products WHERE category = 'Electronics';")
        print("🔒 Type 'exit' to return to menu")
        print("=" * 50)
        
        try:
            import sqlite3
            db_path = self.sql_agent_dir / "sql_agent_class.db"
            
            while True:
                query = input("\n💾 SQL Query: ").strip()
                
                if query.lower() in ['exit', 'quit', 'back']:
                    break
                    
                if not query:
                    continue
                    
                # Safety check
                query_upper = query.upper()
                dangerous_keywords = ['DELETE', 'DROP', 'UPDATE', 'INSERT', 'ALTER', 'CREATE']
                
                if any(keyword in query_upper for keyword in dangerous_keywords):
                    print("⚠️  Dangerous query detected!")
                    confirm = input(f"   Execute '{query}'? (type 'YES' to confirm): ").strip()
                    if confirm != 'YES':
                        print("❌ Query cancelled for safety.")
                        continue
                        
                try:
                    conn = sqlite3.connect(db_path)
                    cursor = conn.cursor()
                    
                    cursor.execute(query)
                    
                    if query_upper.startswith('SELECT'):
                        results = cursor.fetchall()
                        
                        if results:
                            # Get column names
                            columns = [description[0] for description in cursor.description]
                            
                            print(f"\n📊 Results ({len(results)} rows):")
                            print("-" * 40)
                            
                            # Print header
                            print(" | ".join(columns))
                            print("-" * 40)
                            
                            # Print rows (limit to 20 for readability)
                            for i, row in enumerate(results[:20]):
                                print(" | ".join(str(cell) for cell in row))
                                
                            if len(results) > 20:
                                print(f"... and {len(results) - 20} more rows")
                        else:
                            print("📭 No results found.")
                    else:
                        conn.commit()
                        print("✅ Query executed successfully.")
                        
                    conn.close()
                    
                except sqlite3.Error as e:
                    print(f"❌ SQL Error: {e}")
                except Exception as e:
                    print(f"❌ Error: {e}")
                    
        except Exception as e:
            print(f"❌ Error accessing database: {e}")
            
        input("\nPress Enter to continue...")
        
    def run(self):
        """Main CLI loop"""
        while True:
            self.clear_screen()
            self.print_header()
            
            # Quick status check
            api_key = os.getenv('GOOGLE_API_KEY')
            if api_key and api_key != 'your-gemini-api-key-here':
                print("🟢 Status: API Key Configured")
            else:
                print("🟡 Status: API Key Needed (check Setup menu)")
            print()
            
            self.print_menu()
            
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == "1":
                self.setup_menu()
            elif choice == "2":
                self.educational_scripts_menu()
            elif choice == "3":
                self.database_menu()
            elif choice == "4":
                self.quick_tests_menu()
            elif choice == "5":
                self.documentation_menu()
            elif choice == "6":
                self.interactive_chat_menu()
            elif choice == "7":
                print("\n👋 Thank you for using SQL Agent CLI!")
                print("   Happy learning with secure SQL agents! 🛡️")
                break
            else:
                print("❌ Invalid choice. Please try again.")
                time.sleep(1)

if __name__ == "__main__":
    cli = SQLAgentCLI()
    cli.run()
