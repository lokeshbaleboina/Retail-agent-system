def main_agent(state: dict, tools: dict) -> dict:
    """
    Main Sales Agent (LLM Orchestrator).

    For now:
    - Acts as a simple controller
    - Later this will call an LLM to decide routing
    """

    # If no messages yet, greet the user
    if not state.get("messages"):
        state["messages"].append(
            "Hi! I’m your personal shopping assistant 😊 How can I help you today?"
        )
        return state

    last_message = state["messages"][-1].lower()

    # Simple rule-based routing (temporary)
    if "buy" in last_message:
        state["messages"].append(
            "Great choice! Let me help you with the purchase."
        )
    elif "recommend" in last_message:
        state["messages"].append(
            "Sure! Let me find some recommendations for you."
        )
    else:
        state["messages"].append(
            "I can help you with recommendations, availability, or checkout."
        )

    return state
