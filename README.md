🛍️ AI-Powered Omnichannel Retail Sales Agent

EY Techathon 6.0 | Retail & Fashion Commerce

🚀 One-Line Value Proposition

A single AI Sales Agent that follows customers seamlessly across web, WhatsApp, and physical stores, orchestrating specialized agents to deliver personalized, conversion-driven retail experiences.

❓ Problem Statement

Modern retail journeys are fragmented across apps, websites, messaging platforms, and physical stores. Context is lost when customers switch channels, leading to cart abandonment, inconsistent assistance, and missed upsell opportunities—especially during online-to-offline transitions.

💡 Solution Overview

This project implements an Agentic AI–powered Omnichannel Retail Sales Assistant.
A Main LLM-based Sales Agent maintains session context and intelligently coordinates multiple Worker Agents to handle recommendations, inventory checks, store availability, payments, loyalty offers, and post-purchase support.

The system delivers a human-like, continuous sales journey—similar to a top sales associate assisting a customer across channels.

🧠 Why This Is Agentic AI (Not Just a Chatbot)

Main Agent (LLM) reasons, understands intent, and decides next actions

Worker Agents perform specialized domain tasks

LangGraph-style orchestration dynamically routes workflows

MCP architecture cleanly separates reasoning from tool execution

Mental model: A Sales Manager (LLM) delegating tasks to specialist staff (agents).

🔑 Key Capabilities

Personalized product recommendations (LLM-powered)

Real-time inventory and store availability

WhatsApp-style CTAs: BUY NOW, CHECK OFFLINE STORES

Payment link generation

Seamless online → offline handoff

Modular, extensible agent architecture

🧩 System Architecture (High Level)

Flow:

User (Web / WhatsApp / Kiosk)
→ MCP Host (Main Sales Agent)
→ LangGraph Orchestrator
→ Worker Agents
→ MCP Servers & Tools
→ Response to active channel

🤖 Agents Implemented

Main Sales Agent (LLM)

Recommendation Agent (LLM-powered)

Inventory Agent

Store Agent

Payment Agent

Loyalty Agent

Post-Purchase Support Agent

Each Worker Agent communicates with its own MCP Server, enabling independent scaling and fault isolation.

📊 Business Impact Metrics

Cart abandonment ↓

Conversion rate ↑

Average Order Value (AOV) ↑

Cross-channel completion %

Time-to-purchase ↓

🛠️ Technology Stack (Quick View)

Language: Python

Frameworks: FastAPI, LangGraph

LLMs: OpenRouter (OpenAI OSS models)

Architecture: MCP-based microservices

APIs: REST

Data: Synthetic catalog, inventory, customer profiles

⚙️ Run Locally (Quick Start)
git clone https://github.com/lokeshbaleboina/Retail-agent-system.git
cd Retail-agent-system
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt


Create .env:

OPENROUTER_API_KEY=your_openrouter_api_key
OPENROUTER_MODEL=openai/gpt-oss-120b:free


Start services:

uvicorn host.app.main:app --reload --port 8000

🧪 Sample Test
curl -X POST http://localhost:8000/webhook \
-H "Content-Type: application/json" \
-d '{
  "user": {"id":"u1","name":"Lokesh","preferences":["ethnic","formal"]},
  "message":"Suggest something for a wedding"
}'

🔒 Assumptions & Constraints

Inventory, payment, and loyalty systems are mocked for demo purposes

Architecture is production-ready and easily pluggable with real systems

Focus is on agent orchestration and omnichannel continuity

🔮 Future Enhancements

Real WhatsApp Cloud API integration

Voice Assistant Agent

Styling / Gift-Wrapping Agent

Analytics & long-term memory

🏁 Final Note

This project demonstrates how Agentic AI + LLMs + MCP-based microservices can transform fragmented retail touchpoints into a seamless, personalized, revenue-driven omnichannel experience.