"""
graph.py
---------
LangGraph-style orchestration layer.
Controls which agent runs and in what order.
"""

from host.app.agents.main_agent import main_agent
from host.app.mcp_clients import (
    InventoryClient,
    StoreClient,
    PaymentClient,
    RecommendationClient,
    LoyaltyClient,
    ProfileClient,
    SupportClient,
)


def run_graph(state: dict) -> dict:
    """
    Entry point for agent execution.
    This function wires MCP clients + agents together.
    """

    # -------------------------------
    # STEP 1: Initialize MCP Clients
    # -------------------------------
    tools = {
        "inventory": InventoryClient("http://localhost:9001"),
        "store": StoreClient("http://localhost:9002"),
        "payment": PaymentClient("http://localhost:9003"),
        "recommendation": RecommendationClient("http://localhost:9004"),
        "loyalty": LoyaltyClient("http://localhost:9005"),
        "profile": ProfileClient("http://localhost:9006"),
        "support": SupportClient("http://localhost:9007"),
    }

    # -------------------------------
    # STEP 2: Run Main Agent
    # -------------------------------
    final_state = main_agent(state, tools)

    return final_state
