def postpurchase_agent(state: dict, support_client) -> dict:
    order = state.get("order")

    if not order:
        state["messages"].append(
            "I couldn’t find an order yet. Please share your Order ID."
        )
        return state

    order_id = order.get("order_id")

    status = support_client.track_shipment(order_id)

    message = (
        "📦 *Order Status Update*\n\n"
        f"🧾 Order ID: {order_id}\n"
        f"🚚 Status: {status['status']}\n"
    )

    if status["expected_date"]:
        message += f"📅 Expected Delivery: {status['expected_date']}\n"
    if status["courier"]:
        message += f"🏷️ Courier: {status['courier']}"

    state["messages"].append(message)
    return state
