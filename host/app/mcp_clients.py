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

    def get_nearest_stores(self, user_location: str, product_ids: list):
        response = requests.post(
            f"{self.base_url}/getNearestStores",
            json={
                "user_location": user_location,
                "product_ids": product_ids
            },
            timeout=5
        )
        response.raise_for_status()
        return response.json()


class PaymentClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def create_payment(self, user_id: str, amount: float):
        response = requests.post(
            f"{self.base_url}/createPaymentLink",
            json={"user_id": user_id, "amount": amount},
            timeout=5
        )
        response.raise_for_status()
        return response.json()



class RecommendationClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_recommendations(self, occasion: str):
        response = requests.post(
            f"{self.base_url}/getRecommendations",
            json={"occasion": occasion},
            timeout=5
        )
        response.raise_for_status()
        return response.json()



class LoyaltyClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def apply_coupon(self, loyalty_tier: str, amount: float):
        response = requests.post(
            f"{self.base_url}/applyCoupon",
            json={
                "loyalty_tier": loyalty_tier,
                "amount": amount
            },
            timeout=5
        )
        response.raise_for_status()
        return response.json()



class ProfileClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

class SupportClient:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def track_shipment(self, order_id: str):
        response = requests.post(
            f"{self.base_url}/trackShipment",
            json={"order_id": order_id},
            timeout=5
        )
        response.raise_for_status()
        return response.json()

