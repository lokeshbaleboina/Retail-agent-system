import uuid


def create_payment_link(user_id: str, amount: float):
    """
    Simulated payment gateway.
    Returns a dummy payment URL.
    """

    payment_id = str(uuid.uuid4())[:8]

    return {
        "payment_id": payment_id,
        "amount": amount,
        "currency": "INR",
        "payment_url": f"https://pay.example.com/{payment_id}",
        "status": "CREATED"
    }
