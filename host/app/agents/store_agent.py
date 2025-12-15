def store_agent(state: dict, store_client) -> dict:
    cart_items = state.get("cart", {}).get("items", [])
    user_location = state.get("user", {}).get("location", "Hyderabad")

    if not cart_items:
        state["messages"].append(
            "Your cart is empty. Add items to check store availability."
        )
        return state

    product_ids = [item["sku"] for item in cart_items]

    stores = store_client.get_nearest_stores(
        user_location=user_location,
        product_ids=product_ids
    )

    if not stores:
        state["messages"].append(
            "Sorry, these items are not available in nearby stores."
        )
        return state

    responses = []
    for store in stores:
        responses.append(
            f"{store['name']} 📍\n"
            f"{store['address']}\n"
            f"Manager: {store['manager']} ({store['phone']})\n"
            f"Available items: {', '.join(store['available_skus'])}\n"
            f"Directions: {store['maps_url']}"
        )

    state["messages"].append("\n\n".join(responses))
    return state
