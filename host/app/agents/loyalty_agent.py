def loyalty_agent(state: dict, loyalty_client) -> dict:
    user = state.get("user", {})
    cart_items = state.get("cart", {}).get("items", [])

    if not cart_items:
        state["messages"].append("Your cart is empty.")
        return state

    # Simulated cart total
    amount = sum(item.get("price", 999) for item in cart_items)

    loyalty_tier = user.get("loyalty_tier", "BRONZE")

    result = loyalty_client.apply_coupon(
        loyalty_tier=loyalty_tier,
        amount=amount
    )

    message = (
        f"🎉 *Loyalty Benefits Applied!*\n\n"
        f"🏅 Tier: {result['tier']}\n"
        f"💰 Original: ₹{result['original_amount']}\n"
        f"🔻 Discount: ₹{result['discount']}\n"
        f"✅ *Payable Now: ₹{result['final_amount']}*\n\n"
        "Would you like to proceed with payment?"
    )

    state["messages"].append(message)
    state["amount"] = result["final_amount"]
    return state
