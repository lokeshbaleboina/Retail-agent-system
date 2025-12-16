from fastapi import FastAPI
from pydantic import BaseModel
import uuid

app = FastAPI()

class PaymentRequest(BaseModel):
    user_id: str
    amount: float

@app.get("/")
def health():
    return {"status": "Payment MCP Server running"}

@app.post("/createPaymentLink")
def create_payment_link(req: PaymentRequest):
    payment_id = str(uuid.uuid4())
    payment_url = f"https://pay.mock/{payment_id}"

    return {
        "payment_id": payment_id,
        "payment_url": payment_url,
        "amount": req.amount,
        "status": "PENDING"
    }
