# MCP Client stubs
# These will later call real MCP Servers via HTTP

class InventoryClient:
    def __init__(self, base_url: str):
        self.base_url = base_url


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
