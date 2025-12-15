from fastapi import FastAPI
from pydantic import BaseModel
from .tools.trackShipment import track_shipment

app = FastAPI()

class SupportRequest(BaseModel):
    order_id: str

@app.get("/")
def health():
    return {"status": "Support MCP Server running"}

@app.post("/trackShipment")
def track(req: SupportRequest):
    return track_shipment(req.order_id)
