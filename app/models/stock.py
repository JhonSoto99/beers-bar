from datetime import datetime
from typing import List

from pydantic import BaseModel


class Beer(BaseModel):
    """Represents a beer in stock."""

    name: str
    price: int
    quantity: int


class Stock(BaseModel):
    """Represents the stock of beers."""

    last_updated: datetime
    beers: List[Beer]
