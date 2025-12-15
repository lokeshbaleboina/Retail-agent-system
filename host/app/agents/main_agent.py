from host.app.agents.inventory_agent import inventory_agent
from host.app.agents.store_agent import store_agent


def main_agent(state: dict, tools: dict) -> dict:
    # First interaction
    if not state.get("messages"):
        state["messages"].append(
            "Hi! I’m your AI shopping assistant 😊 How can I help you?"
        )
        return state

    last_message = state["messages"][-1].lower()

    # Inventory flow (online stock)
    if "availability" in last_message or "stock" in last_message:
        return inventory_agent(state, tools["inventory"])

    # Store flow (offline / omnichannel)
    if "store" in last_message or "offline" in last_message or "near me" in last_message:
        return store_agent(state, tools["store"])

    # Default fallback
    state["messages"].append(
        "I can help with product recommendations, availability, or nearby stores."
    )
    return state
