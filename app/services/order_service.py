from typing import Dict, List

from app.models.order import Item, Order, Round
from app.repositories.order_repository import OrderRepository
from app.repositories.stock_repository import StockRepository


class OrderService:
    """
    Service class for handling order-related operations.

    This class interacts with order and stock repositories to retrieve,
    process, and update order data.
    """

    def __init__(
        self,
        order_repository: OrderRepository,
        stock_repository: StockRepository,
    ):
        """
        Initializes the OrderService with the given repositories.

        Args:
            order_repository (OrderRepository): The repository for accessing order data.
            stock_repository (StockRepository): The repository for accessing stock data.
        """
        self.order_repository = order_repository
        self.stock_repository = stock_repository

    def get_order_status(self) -> Order:
        """
        Retrieves and calculates the current order status.

        The status includes aggregating items from rounds and calculating
        the subtotal for the order.

        Returns:
            Order: The current order with updated items and subtotal.
        """
        order = self.order_repository.get_order()
        order.items = self.aggregate_items_from_rounds(order.rounds)
        order.subtotal = self.calculate_subtotal(order.items)

        return order

    def aggregate_items_from_rounds(self, rounds: List[Round]) -> List[Item]:
        """
        Aggregates items from all rounds into a summary of items.

        This method iterates through the rounds, summing up the quantity of
        items, and retrieving the price per unit from the stock repository.

        Args:
            rounds (List[Round]): A list of rounds containing order items.

        Returns:
            List[Item]: A list of aggregated items with their total quantities
            and calculated prices.
        """
        stock = {
            beer.name: beer.price
            for beer in self.stock_repository.get_stock().beers
        }
        item_summary = {}

        for round in rounds:
            for round_item in round.items:
                self.update_item_summary(
                    item_summary, round_item.name, round_item.quantity, stock
                )

        return [
            Item(
                name=name,
                price_per_unit=details["price_per_unit"],
                total=details["quantity"] * details["price_per_unit"],
            )
            for name, details in item_summary.items()
        ]

    def update_item_summary(
        self,
        item_summary: Dict,
        name: str,
        quantity: int,
        stock: Dict[str, int],
    ) -> None:
        """
        Helper function to update the item summary.

        If the item already exists in the summary, it updates the quantity.
        Otherwise, it adds the item with its price from stock.

        Args:
            item_summary (Dict): Dictionary summarizing items and their details.
            name (str): The name of the item to add/update.
            quantity (int): The quantity of the item to add.
            stock (Dict[str, int]): A dictionary mapping item names to their prices.
        """
        if name in item_summary:
            item_summary[name]["quantity"] += quantity
        else:
            price_per_unit = stock.get(name, 0)
            item_summary[name] = {
                "quantity": quantity,
                "price_per_unit": price_per_unit,
            }

    def calculate_subtotal(self, items: List[Item]) -> int:
        """
        Calculates the subtotal for an order based on its items.

        Args:
            items (List[Item]): A list of items to calculate the subtotal from.

        Returns:
            int: The total sum of all item prices.
        """
        return sum(item.total for item in items)
