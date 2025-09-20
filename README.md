# 🛡️ SQL Agent Security & Analytics Masterclass

A comprehensive educational project demonstrating secure SQL agent development using **Google Gemini AI** and **LangChain**. Learn to build production-ready SQL agents with proper security guardrails and business intelligence capabilities.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.3.27-green)
![Gemini AI](https://img.shields.io/badge/Gemini-AI-orange)
![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey)

## 🚀 Quick Start

### Interactive CLI (Recommended)

The easiest way to explore this project:

```bash
# Clone the repository
git clone https://github.com/rabiawaqar06/sqldb-agent.git
cd sqldb-agent

# Launch the interactive CLI
./launch_cli.sh          # Linux/Mac
launch_cli.bat            # Windows
# Or directly: python sql_agent_cli.py
```

### Manual Setup

```bash
# 1. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Add your Gemini API key to .env

# 4. Verify setup
python test_setup.py

# 5. Start exploring!
python sql_agent_cli.py
```

## 🎯 What You'll Learn

### Progressive Security Implementation
- **🔓 Basic SQL Agent** → Simple database querying (educational)
- **⚠️ Vulnerable Agent** → What NOT to do (security awareness)
- **🛡️ Secure Agent** → Production-ready with full guardrails
- **📊 Analytics Agent** → Advanced business intelligence

### Security Concepts Covered
- Input validation and SQL injection prevention
- Whitelist-based security (SELECT-only operations)
- Result set limiting and resource protection
- Multi-statement prevention
- Error handling and graceful failures
- Schema-based access controls

## ✨ Key Features

### 🎮 Interactive CLI Interface
- **💬 Chat with Gemini AI** - General purpose conversation
- **🛡️ Secure SQL Agent** - Protected business intelligence queries
- **📊 Business Analytics** - Specialized BI conversations
- **💾 Direct SQL Queries** - Raw database access with safety warnings
- **🔧 Environment Management** - Setup, testing, and troubleshooting

### 📚 Educational Scripts
1. **00_simple_llm.py** - Basic LLM conversation without tools
2. **01_simple_agent.py** - Simple SQL agent (minimal security)
3. **02_risky_delete_demo.py** - Dangerous patterns (educational only)
4. **03_guardrailed_agent.py** - Production-ready secure agent
5. **04_complex_queries.py** - Advanced analytics and BI

### 🗄️ Sample Database
Real e-commerce database with:
- **Customers** (6 records with regions)
- **Products** (6 items across categories)
- **Orders** (12 orders with various statuses)
- **Payments** (payment methods and statuses)
- **Refunds** (refund tracking)
- **Order Items** (detailed line items)

## 🛡️ Security Highlights

### Production-Ready Guardrails
```python
# Input validation with regex patterns
SAFE_QUERY_PATTERN = r'^SELECT\s+'
if not re.match(SAFE_QUERY_PATTERN, query.upper()):
    raise SecurityError("Only SELECT queries allowed")

# Automatic result limiting
query += " LIMIT 200"

# SQL injection prevention
# Multi-statement blocking
# Comprehensive error handling
```

### Multiple Security Levels
- **🔓 Educational** - Minimal restrictions for learning
- **🛡️ Production** - Full security implementation
- **📊 Analytics** - Business-focused with safe operations

## 📊 Sample Business Queries

```sql
-- Revenue by region
SELECT c.region, SUM(p.amount_cents)/100 as revenue
FROM customers c
JOIN orders o ON c.id = o.customer_id
JOIN payments p ON o.id = p.order_id
WHERE p.status = 'succeeded'
GROUP BY c.region;

-- Top selling products
SELECT pr.name, SUM(oi.quantity) as total_sold
FROM products pr
JOIN order_items oi ON pr.id = oi.product_id
GROUP BY pr.id, pr.name
ORDER BY total_sold DESC;
```

## 🔧 Prerequisites

- **Python 3.8+**
- **Google Gemini API Key** ([Get one here](https://makersuite.google.com/app/apikey))
- **Basic SQL and Python knowledge**

## 📁 Project Structure

```
sqldb-agent/
├── 🎮 sql_agent_cli.py              # Interactive CLI interface
├── 🚀 launch_cli.sh / .bat          # Cross-platform launchers
├── 🧪 test_setup.py                 # Environment verification
├── 📦 requirements.txt              # Python dependencies
├── 🔐 .env.example                  # Environment template
├── 📊 demo_cli.py                   # CLI demonstration
└── 📂 SQLAgent/                     # Main educational package
    ├── 📖 README.md                 # Detailed documentation
    ├── 🗄️ sql_agent_class.db        # Sample SQLite database
    ├── 📜 sql_agent_seed.sql        # Database schema and data
    └── 📂 scripts/                  # Progressive tutorial scripts
        ├── 🔄 reset_db.py
        ├── 🤖 00_simple_llm.py
        ├── 🔓 01_simple_agent.py
        ├── ⚠️ 02_risky_delete_demo.py
        ├── 🛡️ 03_guardrailed_agent.py
        └── 📊 04_complex_queries.py
```

## 💬 Interactive Features

### Real-Time AI Interaction
- **Persistent chat sessions** (no timeouts)
- **Natural language to SQL** translation
- **Multiple interaction modes** for different use cases
- **Seamless switching** between chat and SQL

### Business Intelligence Focus
- Revenue analysis and customer insights
- Product performance tracking
- Regional comparison and trends
- Customer lifetime value calculations

## 🔄 Migration from OpenAI

This project has been updated from OpenAI to **Google Gemini AI**:

- ✅ **API Integration**: `langchain_google_genai.ChatGoogleGenerativeAI`
- ✅ **Model**: `gemini-1.5-flash` (efficient and capable)
- ✅ **Agent Types**: Compatible with Gemini's capabilities
- ✅ **Environment**: Uses `GOOGLE_API_KEY`
- ✅ **All Scripts Updated**: Full compatibility maintained

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📚 Learning Path

1. **Start with Setup** - Verify environment and dependencies
2. **Try Interactive Chat** - Get familiar with AI interaction
3. **Follow Educational Scripts** - Progress through 00 → 01 → 03 → 04
4. **Explore Security Features** - Understand guardrails and protections
5. **Build Business Queries** - Practice with analytics scenarios

## ⚠️ Security Warnings

- **Script 02** contains dangerous patterns - **educational only**
- **Always validate inputs** in production environments
- **Use secure agents** for real business applications
- **Review all queries** before execution in production

## 📄 License

This project is for educational purposes. Feel free to use and modify for learning about SQL agent security.

## 🙋‍♀️ Support

- **Interactive CLI Help** - Built-in documentation and troubleshooting
- **Detailed README** - Comprehensive guides in `SQLAgent/README.md`
- **Example Queries** - Sample business intelligence scenarios
- **Security Guidelines** - Best practices for production deployment

---

🎉 **Ready to master secure SQL agents with Google Gemini AI!**

Launch the interactive CLI: `./launch_cli.sh` and start exploring! 🚀
