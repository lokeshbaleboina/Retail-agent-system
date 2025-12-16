# AI-Powered Omnichannel Retail Sales Agent  
### EY Techathon 6.0 | Retail & Fashion Commerce

---

## 1. Executive Summary
This project presents an **Agentic AI–powered Omnichannel Retail Sales Assistant** that delivers a continuous, context-aware shopping experience across web, WhatsApp, and physical retail touchpoints.

A **central AI Sales Agent (LLM-based)** orchestrates multiple specialized Worker Agents to guide customers through discovery, availability checks, checkout, and post-purchase support—similar to a skilled in-store sales associate operating across channels.

---

## 2. Problem Statement
Modern retail journeys are fragmented across websites, mobile apps, messaging platforms, and physical stores. When customers switch channels:

- Context is lost  
- Assistance becomes inconsistent  
- Cart abandonment increases  
- Upsell and cross-sell opportunities are missed  

Retailers lack a system that can **maintain session continuity and sales intent across channels**, especially during online-to-offline transitions.

---

## 3. Solution Overview
The solution implements an **Agentic AI architecture** with a clear separation of responsibilities:

- A **Main Sales Agent (LLM)** that understands user intent, maintains session context, and decides next actions
- Multiple **Worker Agents** that execute domain-specific tasks via tools

This architecture enables a **human-like, uninterrupted sales journey**, regardless of how or where the customer interacts.

---

## 4. Why This Is Agentic AI (Not a Chatbot)
This system goes beyond scripted chatbots:

- The **Main Agent reasons** over conversation history and user intent
- **Worker Agents act autonomously** on specific tasks (inventory, payment, loyalty, etc.)
- **Dynamic orchestration** routes requests at runtime
- Supports **multi-step workflows**, not single-turn responses

The result is goal-oriented, adaptive behavior rather than predefined flows.

---

## 5. Target Users
- **Industry:** Retail & Fashion Commerce  
- **Business Model:** B2C  
- **End Users:** Shoppers using web, mobile apps, WhatsApp, and in-store kiosks  
- **Internal Stakeholders:** Customer Experience, Retail Sales, Store Operations  

---

## 6. Omnichannel User Journey (Scenario)
1. Customer browses products on web or mobile app
2. AI Sales Agent provides personalized recommendations
3. Conversation continues on WhatsApp for reminders or follow-ups
4. Customer visits a physical store; session is restored at a kiosk
5. Agent checks store inventory and suggests bundles
6. Payment link is generated or items are reserved for in-store trial
7. Post-purchase tracking and support continue on the preferred channel

---

## 7. System Architecture (Conceptual)
- **MCP Host:**  
  - Main Sales Agent (LLM)  
  - Orchestration / routing logic  

- **Worker Agents:**  
  - Recommendation  
  - Inventory  
  - Store Availability  
  - Payment  
  - Loyalty & Offers  
  - Fulfillment  
  - Post-Purchase Support  

- **MCP Servers:**  
  Backend microservices exposing tools for each domain

---

## 8. Data & Control Flow
User Request
→ API Gateway
→ Main Sales Agent (Orchestrator)
→ Worker Agent
→ MCP Client
→ MCP Server (Tool Execution)
→ Structured Response
→ User-facing Channel

Session state, cart data, and preferences are preserved and reused across channels.

---

## 9. Impact Metrics
- Cart abandonment reduction  
- Conversion rate improvement  
- Average Order Value (AOV) increase  
- Cross-channel completion rate  
- Engagement rate  
- Reduced time-to-purchase  

---

## 10. Technology Stack
- **Backend:** Python, FastAPI  
- **AI / Orchestration:** LLM-based Main Agent, LangGraph-style routing  
- **Architecture:** Microservices, MCP (Model Context Protocol)  
- **APIs:** REST APIs, WhatsApp Cloud API (simulated)  
- **Data:** Synthetic users, mock catalog, inventory, payment stubs  

---

## 11. Assumptions & Design Decisions
- Customer, inventory, loyalty, and payment systems are simulated
- Architecture is **modular and loosely coupled**
- Worker Agents can be added or replaced without impacting the Main Agent
- WhatsApp chosen due to high conversational engagement and adoption

---

## 12. Scalability & Extensibility
- Independent scaling of Worker Agents
- Fault isolation between services
- Secure API-based communication
- Easy extension for new agents (returns, gift wrap, voice assistant)

---

## 13. Running the Project Locally

### Setup
```bash
git clone https://github.com/lokeshbaleboina/Retail-agent-system.git
cd Retail-agent-system
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Run MCP Host
```bash
uvicorn host.app.main:app --reload --port 8000
```

### Run MCP Servers (Example)
```bash
uvicorn mcp_servers.inventory_server.main:app --port 9001
```

---

## 14. Planned Enhancements (Next Round)

- Richer LLM-driven recommendations  
- Store proximity intelligence  
- WhatsApp payment confirmations  
- Returns and exchange workflows  
- Polished end-to-end demo walkthrough  

---

## Conclusion

This solution demonstrates how **Agentic AI** can unify fragmented retail journeys into a single, intelligent omnichannel sales experience—improving customer satisfaction while driving measurable business outcomes.

---

**Author:** Lokesh Baleboina  
**EY Techathon 6.0 – Retail & Fashion Commerce**

