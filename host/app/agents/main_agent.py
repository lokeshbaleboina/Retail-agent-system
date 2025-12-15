from host.app.agents.inventory_agent import inventory_agent


def main_agent(state: dict, tools: dict) -> dict:
    # First interaction
    if not state.get("messages"):
        state["messages"].append(
            "Hi! I’m your AI shopping assistant 😊 How can I help you?"
        )
        return state

    last_message = state["messages"][-1].lower()

    # Inventory flow
    if "availability" in last_message or "stock" in last_message:
        return inventory_agent(state, tools["inventory"])

    # Default fallback
    state["messages"].append(
        "I can help with recommendations, availability, or checkout."
    )
    return state
