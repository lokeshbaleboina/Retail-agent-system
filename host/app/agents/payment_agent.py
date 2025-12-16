def payment_agent(state: dict, payment_client) -> dict:
    user = state.get("user", {})
    cart_items = state.get("recommended_products", [])

    if not cart_items:
        state["messages"].append(
            "Your cart is empty. Please add items before checkout."
        )
        return state

    total_amount = sum(item["price"] for item in cart_items)

    payment = payment_client.create_payment(
        user_id=user.get("id", "guest"),
        amount=total_amount
    )

    # WhatsApp-style CTA message
    message = (
        f"🛒 *Checkout Ready!*\n\n"
        f"💰 Amount: ₹{total_amount}\n\n"
        f"👉 *BUY NOW*: {payment['payment_url']}\n"
        f"🏬 *CHECK OFFLINE STORES*: Reply `STORE`"
    )

    state["messages"].append(message)
    state["payment"] = payment
    return state
