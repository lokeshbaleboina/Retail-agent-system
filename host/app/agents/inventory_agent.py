def inventory_agent(state: dict, inventory_client) -> dict:
    """
    Inventory Tool Agent:
    - Extracts SKUs from cart
    - Calls Inventory MCP Server
    - Converts JSON → human-readable text
    """

    cart_items = state.get("cart", {}).get("items", [])

    if not cart_items:
        state["messages"].append(
            "Your cart is empty. Add items to check availability."
        )
        return state

    product_ids = [item["sku"] for item in cart_items]

    inventory_data = inventory_client.get_inventory(product_ids)

    responses = []
    for sku, info in inventory_data.items():
        if info["quantity"] > 0:
            responses.append(
                f"{info['name']} is available ({info['quantity']} left) in sizes {', '.join(info['sizes'])}."
            )
        else:
            responses.append(
                f"{info['name']} is currently out of stock."
            )

    state["messages"].append(" ".join(responses))
    return state
