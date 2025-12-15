import json
from pathlib import Path

RULES_DB = Path(__file__).resolve().parent.parent / "rules.json"


def apply_coupon(loyalty_tier: str, amount: float):
    with open(RULES_DB) as f:
        rules = json.load(f)

    tier = rules.get(loyalty_tier, rules["BRONZE"])

    discount = (tier["discount_percent"] / 100) * amount
    discount = min(discount, tier["max_discount"])

    final_amount = amount - discount

    return {
        "original_amount": amount,
        "discount": round(discount, 2),
        "final_amount": round(final_amount, 2),
        "tier": loyalty_tier
    }
