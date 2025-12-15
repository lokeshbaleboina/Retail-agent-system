def payment_agent(state: dict, payment_client) -> dict:
    user = state.get("user", {})
    cart_items = state.get("cart", {}).get("items", [])

    if not cart_items:
        state["messages"].append(
            "Your cart is empty. Add items before checkout."
        )
        return state

    # Simulated price calculation
    amount = 0
    for item in cart_items:
        amount += item.get("price", 999)  # dummy price

    payment = payment_client.create_payment_link(
        user_id=user.get("id"),
        amount=amount
    )

    # WhatsApp-style CTA
    message = (
        "🛍️ *Almost there!*\n\n"
        f"💰 Amount: ₹{payment['amount']}\n\n"
        f"👉 *Pay securely here:* {payment['payment_url']}\n\n"
        "Once payment is done, reply *PAID* to confirm."
    )

    state["messages"].append(message)
    state["payment"] = payment
    return state
