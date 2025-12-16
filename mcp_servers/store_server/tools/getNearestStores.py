import json
from pathlib import Path

STORE_DB = Path(__file__).resolve().parent.parent / "stores.json"


def get_nearest_stores(user_location: str, product_ids: list):
    with open(STORE_DB) as f:
        stores = json.load(f)

    results = []

    for store in stores:
        available = [
            sku for sku in product_ids if sku in store["inventory"]
        ]

        if available:
            results.append({
                "store_id": store["store_id"],
                "name": store["name"],
                "address": store["address"],
                "manager": store["manager"],
                "phone": store["phone"],
                "maps_url": f"https://www.google.com/maps?q={store['lat']},{store['lng']}",
                "available_skus": available
            })

    return results
