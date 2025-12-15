from fastapi import FastAPI
from pydantic import BaseModel
from .tools.applyCoupon import apply_coupon

app = FastAPI()


class LoyaltyRequest(BaseModel):
    loyalty_tier: str
    amount: float


@app.get("/")
def health():
    return {"status": "Loyalty MCP Server running"}


@app.post("/applyCoupon")
def apply_loyalty(req: LoyaltyRequest):
    return apply_coupon(req.loyalty_tier, req.amount)
