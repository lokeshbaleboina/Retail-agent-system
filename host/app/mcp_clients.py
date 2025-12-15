# MCP Client stubs
# These will later call real MCP Servers via HTTP

import requests


class InventoryClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_inventory(self, product_ids: list) -> dict:
        response = requests.post(
            f"{self.base_url}/getInventory",
            json={"product_ids": product_ids},
            timeout=5
        )
        response.raise_for_status()
        return response.json()



class StoreClient:
    def __init__(self, base_url: str):
        self.base_url = base_url


class PaymentClient:
    def __init__(self, base_url: str):
        self.base_url = base_url


class RecommendationClient:
    def __init__(self, base_url: str):
        self.base_url = base_url


class LoyaltyClient:
    def __init__(self, base_url: str):
        self.base_url = base_url


class ProfileClient:
    def __init__(self, base_url: str):
        self.base_url = base_url


class SupportClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
