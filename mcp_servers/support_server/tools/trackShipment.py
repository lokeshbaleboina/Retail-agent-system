import json
from pathlib import Path

DB = Path(__file__).resolve().parent.parent / "shipments.json"

def track_shipment(order_id: str):
    with open(DB) as f:
        data = json.load(f)

    return data.get(order_id, {
        "status": "Order not found",
        "expected_date": None,
        "courier": None
    })
