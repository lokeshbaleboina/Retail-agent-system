from host.app.llm_client import call_llm

SYSTEM_PROMPT = """
You are a friendly fashion retail assistant.
Given products and user context, recommend items naturally.
Do not mention SKUs directly unless asked.
"""

def recommendation_agent(state: dict, rec_client) -> dict:
    last_message = state["messages"][-1]
    user = state.get("user", {})
    cart = state.get("cart", {}).get("items", [])

    # Simple intent extraction
    occasion = "wedding" if "wedding" in last_message.lower() else "general"

    products = rec_client.get_recommendations(occasion)

    user_prompt = f"""
User message: {last_message}
User profile: {user}
Cart items: {cart}
Products: {products}

Suggest 2–3 items in a friendly tone.
"""

    reply = call_llm(SYSTEM_PROMPT, user_prompt)

    state["messages"].append(reply)
    state["recommended_products"] = products
    return state
