from fastapi import FastAPI
from pydantic import BaseModel
from .tools.getNearestStores import get_nearest_stores

app = FastAPI()


class StoreRequest(BaseModel):
    user_location: str
    product_ids: list


@app.get("/")
def health():
    return {"status": "Store MCP Server running"}


@app.post("/getNearestStores")
def nearest_stores(req: StoreRequest):
    return get_nearest_stores(req.user_location, req.product_ids)
