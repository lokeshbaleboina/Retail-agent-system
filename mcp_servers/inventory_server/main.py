from fastapi import FastAPI
from pydantic import BaseModel
from .tools.getInventory import get_inventory


app = FastAPI()


class InventoryRequest(BaseModel):
    product_ids: list


@app.get("/")
def health_check():
    return {"status": "Inventory MCP Server running"}


@app.post("/getInventory")
def inventory_endpoint(request: InventoryRequest):
    """
    MCP Tool Endpoint: getInventory
    """
    return get_inventory(request.product_ids)
