from pydantic import BaseModel
from typing import List
from datetime import datetime

class Item(BaseModel):
    name: str
    price_per_unit: int
    total: int

class Round(BaseModel):
    created: datetime
    items: List[Item]

class Order(BaseModel):
    created: datetime
    paid: bool
    subtotal: int
    taxes: int
    discounts: int
    items: List[Item]
    rounds: List[Round]
