import json
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "mock_db.json"


def get_inventory(product_ids: list) -> dict:
    """
    Inventory tool:
    Input: list of product IDs
    Output: inventory details for each product
    """

    with open(DB_PATH) as f:
        db = json.load(f)

    result = {}

    for pid in product_ids:
        if pid in db:
            result[pid] = db[pid]
        else:
            result[pid] = {
                "name": "Unknown Product",
                "quantity": 0,
                "sizes": []
            }

    return result
