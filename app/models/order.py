from datetime import datetime
from typing import List

from pydantic import BaseModel


class Item(BaseModel):
    """Represents an item in the order."""

    name: str
    price_per_unit: int
    total: int


class RoundItem(BaseModel):
    """Represents an item in a round."""

    name: str
    quantity: int


class Round(BaseModel):
    """Represents a round of items ordered."""

    created: datetime
    items: List[RoundItem]


class Order(BaseModel):
    """Represents an order containing multiple rounds of items."""

    created: datetime
    paid: bool
    subtotal: int
    taxes: int
    discounts: int
    items: List[Item] | None = None
    rounds: List[Round]
