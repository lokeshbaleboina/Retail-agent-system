from fastapi import FastAPI
from pydantic import BaseModel
from .tools.createPaymentLink import create_payment_link

app = FastAPI()


class PaymentRequest(BaseModel):
    user_id: str
    amount: float


@app.get("/")
def health():
    return {"status": "Payment MCP Server running"}


@app.post("/createPaymentLink")
def create_payment(req: PaymentRequest):
    return create_payment_link(req.user_id, req.amount)
